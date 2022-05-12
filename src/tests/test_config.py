from pathlib import Path
from tdeployer.config import Config, Stage
from serde.yaml import from_yaml, to_yaml


def test_stage():
    s = Config(host='test', prefix=Path('test'), stages=[Stage(name='prd', path=Path('/home'))])
    assert s.get_path('prd') == Path('/home')



def test_serde():
    import pathlib
    p = pathlib.Path(__file__)
    with open(p.parent / 'example.yml') as f:
        data = f.read()
    res = from_yaml(Config, data)
    print(res)
