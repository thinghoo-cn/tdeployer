from pathlib import Path

from serde.yaml import from_yaml

from tdeployer.config import Service, Stage


def test_stage():
    s = Service(
        name="qms",
        host="test",
        prefix=Path("test"),
        stages=[Stage(name="prd", path=Path("/home"))],
    )
    assert s.get_path("prd") == Path("/home")


def test_serde():
    import pathlib

    # tests/example.yml
    p = pathlib.Path(__file__)
    with open(p.parent / "example.yml") as f:
        data = f.read()
    res = from_yaml(Service, data)
    assert res.host == "114.114.114.114"
