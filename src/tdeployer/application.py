import pathlib
from typing import Literal
from fabric import Connection
from .config import Config, Stage
from .ciclient import CIClient
from .server import DeployServer


class Application:
    def __init__(self, config: Config, ci_client: CIClient, server: DeployServer) -> None:
        self.config = config
        self.ci_client = ci_client
        self.server = server
