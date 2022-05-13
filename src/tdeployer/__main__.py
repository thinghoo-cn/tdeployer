import pathlib
import argparse

from pkg_resources import require

from tdeployer.application import Application
from tdeployer.config import logger


def cli():
    parser = argparse.ArgumentParser(description='tdeployer is a automation deployer')
    parser.add_argument('command', choices=['update', 'deploy'], help='execute command')
    parser.add_argument('--name', choices=['qms','supply','mes',], required=True, help='project name.')
    parser.add_argument('--stage', choices=['prd', 'test', 'dev', 'demo'], required=True, help='code stage.')
    parser.add_argument('--config-path',
                        dest='config_path',
                        default='/etc/thinghoo/deploy.yml',
                        type=str,
                        help='set config path.')

    args = parser.parse_args()
    logger.info(f'command is: {args.command}')

    config_path = pathlib.Path(args.config_path)
    conf = Application.config_loader(config_path)
    app = Application(config=conf, )

    app.run(cmd=args.command, name=args.name, stage=args.stage)


if __name__ == "__main__":
    cli()