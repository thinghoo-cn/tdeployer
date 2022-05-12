from .ciclient import CIClient
from .config import Config


class Application:
    def __init__(self, config: Config, ci_client: CIClient) -> None:
        self.config = config
        self.ci_client = ci_client
