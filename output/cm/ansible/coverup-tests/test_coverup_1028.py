# file lib/ansible/module_utils/facts/collector.py:54-55
# lines [54, 55]
# branches []

import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

def test_collector_not_found_error():
    with pytest.raises(CollectorNotFoundError) as exc_info:
        raise CollectorNotFoundError("Test error")

    assert str(exc_info.value) == "'Test error'", "CollectorNotFoundError did not contain the correct message"
