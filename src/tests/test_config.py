from pathlib import Path
from tdeployer.config import Service, Stage
from serde.yaml import from_yaml, to_yaml


def test_stage():
    s = Service(name='qms',
                host='test',
                prefix=Path('test'),
                repos=['qms_backend'],
                stages=[Stage(name='prd', path=Path('/home'))])
    assert s.get_path('prd') == Path('/home')


def test_serde():
    import pathlib
    p = pathlib.Path(__file__)
    with open(p.parent / 'example.yml') as f:
        data = f.read()
    res = from_yaml(Service, data)
    assert res.host == '114.114.114.114'
