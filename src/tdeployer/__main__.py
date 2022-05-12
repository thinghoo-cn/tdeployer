from tdeployer.application import Application


if __name__ == "__main__":
    conf = Application.config_loader()
    Application(config=conf, )
