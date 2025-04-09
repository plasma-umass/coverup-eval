# file: lib/ansible/module_utils/facts/collector.py:54-55
# asked: {"lines": [54, 55], "branches": []}
# gained: {"lines": [54, 55], "branches": []}

import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

def test_collector_not_found_error():
    with pytest.raises(CollectorNotFoundError):
        raise CollectorNotFoundError("Collector not found")

    # Ensure that the exception is a subclass of KeyError
    assert issubclass(CollectorNotFoundError, KeyError)
