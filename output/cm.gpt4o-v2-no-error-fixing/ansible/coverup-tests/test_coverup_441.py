# file: lib/ansible/module_utils/api.py:121-131
# asked: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}
# gained: {"lines": [121, 130, 131], "branches": [[130, 0], [130, 131]]}

import pytest
import random
from unittest.mock import patch
from ansible.module_utils.api import generate_jittered_backoff

@pytest.mark.parametrize("retries, delay_base, delay_threshold", [
    (1, 3, 60),
    (5, 2, 30),
    (10, 1, 10),
])
def test_generate_jittered_backoff(retries, delay_base, delay_threshold):
    with patch('random.randint', return_value=1) as mock_randint:
        backoff = list(generate_jittered_backoff(retries, delay_base, delay_threshold))
        assert len(backoff) == retries
        for delay in backoff:
            assert delay == 1
        mock_randint.assert_called()

