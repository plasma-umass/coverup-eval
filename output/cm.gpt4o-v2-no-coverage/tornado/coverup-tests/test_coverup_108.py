# file: tornado/util.py:291-301
# asked: {"lines": [291, 292, 301], "branches": []}
# gained: {"lines": [291, 292, 301], "branches": []}

import pytest
from tornado.util import Configurable

def test_configurable_base():
    with pytest.raises(NotImplementedError):
        Configurable.configurable_base()
