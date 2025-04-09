# file tornado/util.py:291-301
# lines [291, 292, 301]
# branches []

import pytest
from tornado.util import Configurable

class TestConfigurable:
    def test_configurable_base(self):
        class MyConfigurable(Configurable):
            @classmethod
            def configurable_base(cls):
                return super(MyConfigurable, cls).configurable_base()

        with pytest.raises(NotImplementedError):
            MyConfigurable.configurable_base()
