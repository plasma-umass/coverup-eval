# file: tornado/options.py:726-731
# asked: {"lines": [726, 731], "branches": []}
# gained: {"lines": [726], "branches": []}

import pytest
from tornado.options import OptionParser, options

@pytest.fixture
def reset_options():
    # Save the current state of options
    old_options = options._options.copy()
    old_callbacks = options._parse_callbacks.copy()
    yield
    # Restore the original state of options
    options._options.clear()
    options._options.update(old_options)
    options._parse_callbacks.clear()
    options._parse_callbacks.extend(old_callbacks)

def test_add_parse_callback(reset_options):
    callback_called = False

    def sample_callback():
        nonlocal callback_called
        callback_called = True

    # Add the parse callback
    options.add_parse_callback(sample_callback)

    # Simulate the end of option parsing
    options.run_parse_callbacks()

    # Assert that the callback was called
    assert callback_called
