# file tornado/util.py:303-307
# lines [303, 304, 307]
# branches []

import pytest
from tornado.util import Configurable

class TestConfigurable:
    def test_configurable_default(self, mocker):
        class MyConfigurable(Configurable):
            pass

        with pytest.raises(NotImplementedError):
            MyConfigurable.configurable_default()
