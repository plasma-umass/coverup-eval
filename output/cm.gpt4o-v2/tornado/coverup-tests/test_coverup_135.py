# file: tornado/util.py:303-307
# asked: {"lines": [303, 304, 307], "branches": []}
# gained: {"lines": [303, 304, 307], "branches": []}

import pytest
from tornado.util import Configurable

def test_configurable_default():
    with pytest.raises(NotImplementedError):
        Configurable.configurable_default()
