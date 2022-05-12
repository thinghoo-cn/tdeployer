import pathlib
from dataclasses import dataclass
from typing import Dict, List, Literal
from .errors import TDeployerBaseError


@dataclass
class Stage:
    stage: Literal['dev', 'test', 'prd']
    path: pathlib.Path


@dataclass
class Config:
    host: str
    prefix: pathlib.Path
    stages: List[Stage]

    def get_path(self, stage: Literal['dev', 'test', 'prd']):
        for s in self.stages:
            if s.stage == stage:
                return s
        raise TDeployerBaseError('not a valid stage or stage missing.')
