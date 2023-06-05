import gradio as gr
from .utils import load_ct_to_numpy, load_pred_volume_to_numpy, nifti_to_glb
from .inference import run_model


class WebUI:
    def __init__(self, model_name:str = None, class_name:str = "meningioma", cwd:str = "/home/user/app/"):
        # global states
        self.images = []
        self.pred_images = []

        # @TODO: This should be dynamically set based on chosen volume size
        self.nb_slider_items = 150

        self.model_name = model_name
        self.class_name = class_name
        self.cwd = cwd

        # define widgets not to be rendered immediantly, but later on
        self.slider = gr.Slider(1, self.nb_slider_items, value=1, step=1, label="Which 2D slice to show")
        self.volume_renderer = gr.Model3D(
            clear_color=[0.0, 0.0, 0.0, 0.0],
            label="3D Model",
            visible=True,
            elem_id="model-3d",
        ).style(height=512)

    def combine_ct_and_seg(self, img, pred):
        return (img, [(pred, self.class_name)])
    
    def upload_file(self, file):
        return file.name
    
    def load_mesh(self, mesh_file_name):
        path = mesh_file_name.name
        run_model(path, model_path=self.cwd + "resources/models/")
        nifti_to_glb("prediction.nii.gz")

        self.images = load_ct_to_numpy(path)
        self.pred_images = load_pred_volume_to_numpy("./prediction.nii.gz")
        self.slider = self.slider.update(value=2)
        return "./prediction.obj"
    
    def get_img_pred_pair(self, k):
        k = int(k) - 1
        out = [gr.AnnotatedImage.update(visible=False)] * self.nb_slider_items
        out[k] = gr.AnnotatedImage.update(self.combine_ct_and_seg(self.images[k], self.pred_images[k]), visible=True)
        return out

    def run(self):
        css="""
        #model-3d {
        height: 512px;
        }
        #model-2d {
        height: 512px;
        margin: auto;
        }
        """
        with gr.Blocks(css=css) as demo:

            with gr.Row():
                file_output = gr.File(
                    file_count="single"
                ).style(full_width=False, size="sm")
                file_output.upload(self.upload_file, file_output, file_output)

                run_btn = gr.Button("Run analysis").style(full_width=False, size="sm")
                run_btn.click(
                    fn=lambda x: self.load_mesh(x),
                    inputs=file_output,
                    outputs=self.volume_renderer
                )
            
            with gr.Row():
                gr.Examples(
                    examples=[self.cwd + "RegLib_C01_2.nii"],
                    inputs=file_output,
                    outputs=file_output,
                    fn=self.upload_file,
                    cache_examples=True,
                )
            
            with gr.Row():
                with gr.Box():
                    image_boxes = []
                    for i in range(self.nb_slider_items):
                        visibility = True if i == 1 else False
                        t = gr.AnnotatedImage(visible=visibility, elem_id="model-2d")\
                            .style(color_map={self.class_name: "#ffae00"}, height=512, width=512)
                        image_boxes.append(t)

                    self.slider.change(self.get_img_pred_pair, self.slider, image_boxes)
                
                with gr.Box():
                    self.volume_renderer.render()
            
            with gr.Row():
                self.slider.render()

        # sharing app publicly -> share=True: https://gradio.app/sharing-your-app/
        # inference times > 60 seconds -> need queue(): https://github.com/tloen/alpaca-lora/issues/60#issuecomment-1510006062
        demo.queue().launch(server_name="0.0.0.0", server_port=7860, share=True)
