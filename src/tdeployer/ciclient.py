import pathlib
from fabric import Connection
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
            self.c.run('docker-compose restart nginx')

    def update(self, path: pathlib.Path, stage: stage_constraint):
        """
        登陆到某台服务器上运行更新服务器命令
        """
        with self.c.cd(str(path)):
            # 可以考虑在本地构建 compose，然后在过程做拉取
            self.c.run(f'tbuilder update --stage {stage}')
