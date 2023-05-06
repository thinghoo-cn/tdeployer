import pathlib
import sys

import invoke
from fabric import Connection
from typing import List, Literal


class ControlClient:
    def __init__(self, connection: Connection) -> None:
        self.c = connection

    def deploy(self, pathlist: List[str]):
        """更新远程服务器的服务

        Args:
            path (str): _description_
        """
        for path in pathlist:
            try:
                with self.c.cd(str(path)):
                    self.c.run("git pull")
                    self.c.run("docker-compose up -d --build")
                    self.c.run("docker-compose restart nginx")
            except invoke.exceptions.UnexpectedExit:
                # TODO: log to files.
                print("CD server meet error.", file=sys.stderr)
                sys.exit(-1)

    def update(self, pathlist: List[str], stage: str):
        """
        登陆到某台服务器上运行更新服务器命令
        """
        for path in pathlist:
            print(path)
            try:
                with self.c.cd(str(path)):
                    # 可以考虑在本地构建 compose，然后在过程做拉取
                    self.c.run(f"tbuilder pull --stage {stage}")
            except invoke.exceptions.UnexpectedExit:
                # TODO: log to files.
                print("CD server meet error.", file=sys.stderr)
                sys.exit(-1)
