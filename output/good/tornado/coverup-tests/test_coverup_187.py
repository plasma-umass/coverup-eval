# file tornado/options.py:551-552
# lines [551, 552]
# branches []

import pytest
from tornado.options import _Option, OptionParser

@pytest.fixture
def option_cleanup():
    # Fixture to clean up OptionParser after the test
    parser = OptionParser()
    yield
    parser._options.clear()
    parser._parse_callbacks.clear()

def test_option_value(option_cleanup):
    # Test to cover the _Option.value method
    opt = _Option(name='test_option', default='default_value', type=str)
    assert opt.value() == 'default_value', "The default value should be returned when _value is UNSET"

    # Set a new value and check if it is returned
    opt._value = 'new_value'
    assert opt.value() == 'new_value', "The new value should be returned when _value is set"
