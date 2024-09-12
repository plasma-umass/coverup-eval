# file: lib/ansible/module_utils/api.py:121-131
# asked: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}
# gained: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}

import pytest
import random
from ansible.module_utils.api import generate_jittered_backoff

def test_generate_jittered_backoff(monkeypatch):
    retries = 5
    delay_base = 2
    delay_threshold = 10

    # Mock random.randint to return a predictable value
    def mock_randint(start, end):
        return end

    monkeypatch.setattr(random, 'randint', mock_randint)

    backoff = list(generate_jittered_backoff(retries, delay_base, delay_threshold))

    # Verify the length of the backoff list
    assert len(backoff) == retries

    # Verify the values in the backoff list
    for i in range(retries):
        expected_value = min(delay_threshold, delay_base * 2 ** i)
        assert backoff[i] == expected_value
