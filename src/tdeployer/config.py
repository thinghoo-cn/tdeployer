import pathlib
from dataclasses import dataclass
from serde import serde
from typing import Dict, List, Literal
from .errors import TDeployerBaseError


stage_constraint = Literal["dev", "test", "prd", 'demo']

@dataclass
@serde
class Stage:
    name: stage_constraint
    path: pathlib.Path


@dataclass
@serde
class Config:
    host: str
    prefix: pathlib.Path
    stages: List[Stage]

    def get_path(self, stage: stage_constraint):
        for s in self.stages:
            if s.name == stage:
                return s.path
        raise TDeployerBaseError("not a valid stage or stage missing.")
