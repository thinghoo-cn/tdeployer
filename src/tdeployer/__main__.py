import argparse
import pathlib

from tdeployer import __version__
from tdeployer.application import Application
from tdeployer.config import logger


def cli():
    parser = argparse.ArgumentParser(
        description=f"tdeployer is a automation deployer. version: {__version__}, Updating the confirmed code to cdserver."
    )
    parser.add_argument("command", choices=["update", "deploy"], help="execute command")
    parser.add_argument("--name", required=True, help="project name.")
    parser.add_argument(
        "--stage",
        required=True,
        help="code stage.",
    )
    parser.add_argument(
        "--config-path",
        dest="config_path",
        default="/etc/thinghoo/deploy.yml",
        type=str,
        help="set config path.",
    )

    args = parser.parse_args()
    logger.info(f"command is: {args.command}")

    config_path = pathlib.Path(args.config_path)
    conf = Application.config_loader(config_path)
    app = Application(
        config=conf,
    )

    app.run(cmd=args.command, name=args.name, stage=args.stage)


if __name__ == "__main__":
    cli()
