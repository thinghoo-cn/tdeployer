import argparse

from tdeployer.application import Application
from tdeployer.config import logger


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tdeployer is a automation deployer')
    parser.add_argument('command', choices=['update', 'update_code', 'deploy'], help='execute command')

    args = parser.parse_args()
    logger.info(f'command is: {args.command}')
    conf = Application.config_loader()
    Application(config=conf, )
