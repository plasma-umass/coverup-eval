# file lib/ansible/module_utils/common/parameters.py:503-538
# lines [506]
# branches ['505->506']

import pytest
from ansible.module_utils.common.parameters import _sanitize_keys_conditions
from ansible.module_utils.six import text_type, binary_type

@pytest.fixture
def cleanup_deferred_removals():
    deferred_removals = []
    yield deferred_removals
    del deferred_removals[:]

def test_sanitize_keys_conditions_with_string_types(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals

    text_value = text_type("some text")
    binary_value = binary_type(b"some binary data")

    # Test with text_type
    result_text = _sanitize_keys_conditions(text_value, no_log_strings, ignore_keys, deferred_removals)
    assert result_text == text_value
    assert len(deferred_removals) == 0

    # Test with binary_type
    result_binary = _sanitize_keys_conditions(binary_value, no_log_strings, ignore_keys, deferred_removals)
    assert result_binary == binary_value
    assert len(deferred_removals) == 0
