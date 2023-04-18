import pathlib
import sys
from typing import Optional

from serde.yaml import from_yaml

from .ciclient import ControlClient
from .config import TotalConfig, logger
from .errors import InvalidCommand


class Application:
    def __init__(self, config: TotalConfig) -> None:
        self.config = config
        self.client: Optional[ControlClient] = None

    def run(self, name: str, cmd: str, stage: stage_constraint):
        service = self.config.get_service(name=name)
        conn = service.get_connection()
        self.client = ControlClient(connection=conn)

        if cmd == "update":
            self.client.update(service.get_path(stage=stage), stage=stage)
        elif cmd == "deploy":
            self.client.deploy(service.get_path(stage=stage))
        else:
            print(f"invalid cmd: <{cmd}>.")

    @staticmethod
    def config_loader(path: pathlib.Path = pathlib.Path("./deploy.yml")):
        conf_file = pathlib.Path(path)
        if not conf_file.exists():
            logger.error("missing deploy.yml")
            sys.exit(1)

        data = conf_file.read_text()
        conf = from_yaml(TotalConfig, data)
        return conf
