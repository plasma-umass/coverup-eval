# file lib/ansible/module_utils/api.py:96-118
# lines [98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118]
# branches ['102->exit', '102->103', '104->105', '106->107', '106->108', '112->113', '112->114']

import pytest
import time
from unittest.mock import Mock, patch

# Assuming the retry function is defined in ansible.module_utils.api
from ansible.module_utils.api import retry

def test_retry_decorator_exceeds_retries(mocker):
    mock_function = Mock(side_effect=Exception("Test Exception"))
    retries = 3
    retry_pause = 0.1

    decorated_function = retry(retries=retries, retry_pause=retry_pause)(mock_function)

    with pytest.raises(Exception) as excinfo:
        decorated_function()

    assert str(excinfo.value) == f"Retry limit exceeded: {retries}"
    assert mock_function.call_count == retries - 1

def test_retry_decorator_succeeds(mocker):
    mock_function = Mock(side_effect=[Exception("Test Exception"), Exception("Test Exception"), "Success"])
    retries = 4
    retry_pause = 0.1

    decorated_function = retry(retries=retries, retry_pause=retry_pause)(mock_function)

    result = decorated_function()

    assert result == "Success"
    assert mock_function.call_count == 3
