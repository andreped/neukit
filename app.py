from neukit.gui import WebUI


def main():
    print("Launching demo...")

    # cwd = "/Users/andreped/workspace/neukit/"  # local testing -> macOS
    cwd = "/home/user/app/"  # production -> docker

    # initialize and run app
    app = WebUI(cwd=cwd)
    app.run()


if __name__ == "__main__":
    main()
