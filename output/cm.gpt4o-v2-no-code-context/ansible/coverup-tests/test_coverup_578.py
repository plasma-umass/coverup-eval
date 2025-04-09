# file: lib/ansible/module_utils/api.py:121-131
# asked: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}
# gained: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}

import pytest
import random
from ansible.module_utils.api import generate_jittered_backoff

def test_generate_jittered_backoff(monkeypatch):
    # Mock random.randint to return a predictable value
    def mock_randint(start, end):
        return end

    monkeypatch.setattr(random, 'randint', mock_randint)

    retries = 5
    delay_base = 2
    delay_threshold = 10

    backoff_generator = generate_jittered_backoff(retries, delay_base, delay_threshold)
    backoff_list = list(backoff_generator)

    # Verify the length of the generated backoff list
    assert len(backoff_list) == retries

    # Verify that the values are within the expected range
    for i, backoff in enumerate(backoff_list):
        expected_max = min(delay_threshold, delay_base * 2 ** i)
        assert backoff == expected_max
