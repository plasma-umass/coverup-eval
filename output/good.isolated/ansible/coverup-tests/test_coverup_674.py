# file lib/ansible/module_utils/api.py:121-131
# lines [121, 130, 131]
# branches ['130->exit', '130->131']

import pytest
from ansible.module_utils.api import generate_jittered_backoff
from unittest.mock import patch
import random

@pytest.fixture
def random_seed():
    random.seed(0)
    yield
    random.seed()  # Reset the random seed after the test

def test_generate_jittered_backoff(random_seed):
    retries = 5
    delay_base = 2
    delay_threshold = 10
    expected_delays = [0, 1, 2, 4, 8]

    with patch('random.randint', side_effect=expected_delays) as mock_randint:
        backoff_generator = generate_jittered_backoff(retries, delay_base, delay_threshold)
        actual_delays = list(backoff_generator)

        assert len(actual_delays) == retries
        assert all(0 <= delay <= delay_threshold for delay in actual_delays)
        assert actual_delays == expected_delays
        assert mock_randint.call_count == retries
        for i, call in enumerate(mock_randint.call_args_list):
            args, kwargs = call
            assert args[0] == 0
            assert args[1] == min(delay_threshold, delay_base * 2 ** i)
