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

    def run(self, name: str, cmd: str, stage: str):
        service = self.config.get_service(name=name)
        conn = service.get_connection()
        self.client = ControlClient(connection=conn)
        pathlist = service.get_path(stage=stage)

        if cmd == "update":
            for path in pathlist:
                self.client.update(path, stage=stage)
        elif cmd == "deploy":
            for path in pathlist:
                self.client.deploy(path)
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
