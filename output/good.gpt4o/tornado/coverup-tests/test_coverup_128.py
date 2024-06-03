# file tornado/util.py:303-307
# lines [303, 304, 307]
# branches []

import pytest
from tornado.util import Configurable

def test_configurable_default_not_implemented():
    with pytest.raises(NotImplementedError):
        Configurable.configurable_default()
