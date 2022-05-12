import sys
from fabric import Connection
from .ciclient import CIClient
from .config import Config, logger
from serde.yaml import from_yaml, to_yaml


class Application:
    def __init__(self, config: Config) -> None:
        self.config = config

        c = Connection(host=self.config.host, user="root", port=22)
        self.ci_client = CIClient(c)

    @staticmethod
    def config_loader():
        import pathlib
        conf_file = pathlib.Path('./deploy.yml')
        if not conf_file.exists():
            logger.error('missing deploy.yml')
            sys.exit(1)

        data = conf_file.read_text()
        conf = from_yaml(Config, data)
        return conf
