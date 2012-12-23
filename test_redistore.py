import pytest
import pretend

import flask
from flask.ext.redistore import Redistore


@pytest.fixture
def app():
    app = flask.Flask("__main__")
    return app


@pytest.fixture
def redis(app):
    fake_redis = pretend.stub(
            get=lambda _: "WORKS",
        )
    return Redistore(app, redis_class=pretend.stub(from_url=lambda _: fake_redis))


def test_redirection(redis):
    assert redis.get("test") == "WORKS"
