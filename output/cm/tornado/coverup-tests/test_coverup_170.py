# file tornado/options.py:518-523
# lines [518, 522]
# branches []

import pytest
from tornado.options import _Option

def test_option_unset():
    # Since _Option requires a 'name' and 'type' argument, we provide dummy ones
    option = _Option(name='dummy_option', type=str)
    assert option.UNSET is not None

    # Cleanup is not necessary here as we are not modifying any global state
    # and _Option.UNSET is a static value that should not change.
