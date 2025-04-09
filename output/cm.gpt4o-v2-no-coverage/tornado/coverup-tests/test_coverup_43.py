# file: tornado/util.py:321-336
# asked: {"lines": [321, 322, 330, 331, 332, 333, 334, 335, 336], "branches": [[331, 332], [331, 333], [333, 334], [333, 335]]}
# gained: {"lines": [321, 322, 330, 331, 332, 333, 334, 335, 336], "branches": [[331, 332], [331, 333], [333, 334], [333, 335]]}

import pytest
from unittest.mock import patch
from typing import Type
from tornado.util import Configurable

class DummyConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return Configurable

    @classmethod
    def configurable_default(cls):
        return cls

def import_object(name):
    if name == "DummyConfigurable":
        return DummyConfigurable
    raise ImportError

@pytest.fixture
def patch_import_object(monkeypatch):
    monkeypatch.setattr("tornado.util.import_object", import_object)
    monkeypatch.setattr(Configurable, 'configurable_base', DummyConfigurable.configurable_base)

def test_configure_with_string_impl(patch_import_object):
    Configurable.configure("DummyConfigurable", foo="bar")
    assert Configurable._Configurable__impl_class == DummyConfigurable
    assert Configurable._Configurable__impl_kwargs == {"foo": "bar"}

def test_configure_with_class_impl(patch_import_object):
    Configurable.configure(DummyConfigurable, foo="bar")
    assert Configurable._Configurable__impl_class == DummyConfigurable
    assert Configurable._Configurable__impl_kwargs == {"foo": "bar"}

def test_configure_with_none_impl(patch_import_object):
    Configurable.configure(None, foo="bar")
    assert Configurable._Configurable__impl_class is None
    assert Configurable._Configurable__impl_kwargs == {"foo": "bar"}

def test_configure_with_invalid_impl(patch_import_object):
    with pytest.raises(ValueError):
        Configurable.configure(str, foo="bar")
