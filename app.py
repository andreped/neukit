from neukit.gui import WebUI
from argparse import ArgumentParser
import os


def main():
    parser = ArgumentParser()
    parser.add_argument("--cwd", type=str, default="/home/user/app/", help="Set current working directory (path to app.py).")
    parser.add_argument("--share", type=int, default=1, help="Whether to enable the app to be accessible online -> setups a public link which requires internet access.")
    args = parser.parse_args()

    print("Current working directory:", args.cwd)

    if not os.path.exists(args.cwd):
        raise ValueError("Chosen 'cwd' is not a valid path!")
    if not args.share in [0, 1]:
        raise ValueError("The 'share' argument can only be set to 0 or 1 (boolean), but was:", args.share)

    # initialize and run app
    print("Launching demo...")
    app = WebUI(cwd=args.cwd, share=args.share)
    app.run()


if __name__ == "__main__":
    main()
