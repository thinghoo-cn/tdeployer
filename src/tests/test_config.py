from pathlib import Path
from tdeployer.config import Config, Stage


def test_stage():
    s = Config(host='test', prefix=Path('test'), stages=[Stage(stage='prd', path=Path('/home'))])
    assert s.get_path('prd') == Path('/home')
