import os
import sys
import pathlib
from dataclasses import dataclass
from typing import List, Literal

from dotenv import find_dotenv, load_dotenv
from fabric import Connection
from loguru import logger
from serde import serde

from .errors import ServiceNotFound, TDeployerBaseError

load_dotenv(find_dotenv())


@dataclass
@serde
class Stage:
    name: str
    path: List[str]


@dataclass
@serde
class Service:
    name: str
    host: str
    prefix: pathlib.Path
    stages: List[Stage]

    def get_path(self, stage: str) -> List[str]:
        for s in self.stages:
            if s.name == stage:
                return s.path
        print(f'{stage} is not a valid stage or stage missing', file=sys.stderr)
        sys.exit(-1)
        # raise TDeployerBaseError("not a valid stage or stage missing.")

    def get_connection(self):
        c = Connection(host=self.host, user="root", port=22)
        return c


@dataclass
@serde
class TotalConfig:
    version: str
    services: List[Service]

    def get_service(self, name: str) -> Service:
        for s in self.services:
            if name == s.name:
                return s
        raise ServiceNotFound(f"service.{name} not found.")


if not os.getenv("DEBUG"):
    logger.add("/var/log/thinghoo/deploy.log")
