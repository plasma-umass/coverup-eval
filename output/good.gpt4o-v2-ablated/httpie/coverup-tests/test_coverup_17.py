# file: httpie/context.py:116-120
# asked: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}
# gained: {"lines": [116, 117, 118, 119, 120], "branches": [[118, 119], [118, 120]]}

import os
import pytest

from httpie.context import Environment

@pytest.fixture
def environment():
    env = Environment()
    yield env
    if env._devnull is not None:
        env._devnull.close()

def test_devnull_initially_none(environment, monkeypatch):
    monkeypatch.setattr(environment, '_devnull', None, raising=False)
    assert environment._devnull is None

def test_devnull_opened(environment, monkeypatch):
    monkeypatch.setattr(environment, '_devnull', None, raising=False)
    devnull = environment.devnull
    assert devnull is not None
    assert not devnull.closed

def test_devnull_reuse(environment, monkeypatch):
    monkeypatch.setattr(environment, '_devnull', None, raising=False)
    devnull1 = environment.devnull
    devnull2 = environment.devnull
    assert devnull1 is devnull2
    assert not devnull1.closed
