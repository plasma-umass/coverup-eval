# file tornado/options.py:518-523
# lines [518, 522]
# branches []

import pytest
from tornado.options import OptionParser

def test_option_unset():
    class _Option(object):
        UNSET = object()

    option = _Option()
    assert option.UNSET is not None
    assert isinstance(option.UNSET, object)
