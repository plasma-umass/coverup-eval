# file lib/ansible/module_utils/api.py:121-131
# lines [121, 130, 131]
# branches ['130->exit', '130->131']

import pytest
import random
from unittest.mock import patch
from ansible.module_utils.api import generate_jittered_backoff

def test_generate_jittered_backoff(mocker):
    # Mock random.randint to control the output
    mock_randint = mocker.patch('random.randint', side_effect=lambda a, b: b)

    retries = 5
    delay_base = 2
    delay_threshold = 10

    backoff_generator = generate_jittered_backoff(retries=retries, delay_base=delay_base, delay_threshold=delay_threshold)
    backoff_list = list(backoff_generator)

    # Verify the length of the generated backoff list
    assert len(backoff_list) == retries

    # Verify that the values are within the expected range
    for i, delay in enumerate(backoff_list):
        expected_max_delay = min(delay_threshold, delay_base * 2 ** i)
        assert delay == expected_max_delay

    # Verify that random.randint was called with the correct parameters
    for i in range(retries):
        mock_randint.assert_any_call(0, min(delay_threshold, delay_base * 2 ** i))
