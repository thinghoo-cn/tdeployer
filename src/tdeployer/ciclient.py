import pathlib
from datetime import datetime
from fabric import Connection
from typing import Literal, List


class CIClient:
    def __init__(self, connection: Connection) -> None:
        self.c = connection

    def update_command(self, stage: str) -> str:
        command = f'inv update --stage="{stage}"'
        return command

    def _deploy(self, host, path: pathlib.Path, command):
        """
        登陆到某台服务器上运行更新服务器命令
        """
        conn = Connection(host=host, user="root", port=22)

        with conn.cd(str(path)):
            conn.run(command)

    def update(self, repos: List[str], stage: Literal['prd', 'test', 'dev']):
        """this repo depends on tbuilder.

        Args:
            repos (Repo): _description_
        """
        # repos = ['qms_backend', 'qms_frontend']
        for r in repos:
            with self.c.cd(r):
                self.c.run('git reset --hard')
                self.c.run(f'git pull origin {stage}')

        self.c.run('git pull')
        self.c.run('git add .')
        self.c.run(f'git commit --allow-empty -m "feat: update remote repository at {datetime.now().date()}"')
        self.c.run('git push')

    def deploy(self, stage='dev'):
        if stage == 'demo':
            path = '/root/services/qms-compose-demo'
        elif stage == 'dev':
            path = '/root/services/qms-compose'
        elif stage == "test":
            path = '/root/services/qms-compose-test'
        else:
            assert False, "Invalid stage."

        with self.c.cd(path):
            self.c.run('git pull')
            self.c.run('docker-compose up -d --build')