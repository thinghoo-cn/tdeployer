import pathlib
from dataclasses import dataclass
from typing import Dict, List, Literal
from .errors import TDeployerBaseError


stage_constraint = Literal["dev", "test", "prd", 'demo']

@dataclass
class Stage:
    stage: stage_constraint
    path: pathlib.Path


@dataclass
class Config:
    host: str
    prefix: pathlib.Path
    stages: List[Stage]

    def get_path(self, stage: stage_constraint):
        for s in self.stages:
            if s.stage == stage:
                return s.path
        raise TDeployerBaseError("not a valid stage or stage missing.")
