# file tornado/util.py:309-310
# lines [309, 310]
# branches []

import pytest
from tornado.util import Configurable

class DummyConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return DummyConfigurable

    @classmethod
    def configurable_default(cls):
        return DummyConfigurable

    def _initialize(self) -> None:
        super()._initialize()

def test_initialize(mocker):
    mocker.patch.object(DummyConfigurable, '_initialize')
    configurable_instance = DummyConfigurable()
    configurable_instance._initialize()

    # Assert that the _initialize method was called
    assert DummyConfigurable._initialize.called
