import pathlib
from datetime import datetime
from fabric import Connection
from typing import Literal, List
from .config import stage_constraint


class ControlClient:
    def __init__(self, connection: Connection) -> None:
        self.c = connection

    def deploy(self, path: pathlib.Path):
        """更新远程服务器的服务

        Args:
            path (str): _description_
        """
        with self.c.cd(str(path)):
            self.c.run("git pull")
            self.c.run("docker-compose up -d --build")

    def update(self, path: pathlib.Path, stage: stage_constraint):
        """
        登陆到某台服务器上运行更新服务器命令
        """
        with self.c.cd(str(path)):
            self.c.run(f'inv update --stage="{stage}"')

    def update_repos(self, repos: List[str], stage: stage_constraint):
        """this repo depends on tbuilder.

        Args:
            repos (Repo): _description_
        """
        # repos = ['qms_backend', 'qms_frontend']
        for r in repos:
            with self.c.cd(r):
                self.c.run("git reset --hard")
                self.c.run(f"git pull origin {stage}")

        self.c.run("git pull")
        self.c.run("git add .")
        self.c.run(
            f'git commit --allow-empty -m "feat: update remote repository at {datetime.now().date()}"'
        )
        self.c.run("git push")
