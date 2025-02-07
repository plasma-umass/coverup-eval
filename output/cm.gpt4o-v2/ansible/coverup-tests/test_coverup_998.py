# file: lib/ansible/module_utils/facts/collector.py:54-55
# asked: {"lines": [54, 55], "branches": []}
# gained: {"lines": [54, 55], "branches": []}

import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

def test_collector_not_found_error():
    with pytest.raises(CollectorNotFoundError):
        raise CollectorNotFoundError("Collector not found")

    try:
        raise CollectorNotFoundError("Collector not found")
    except CollectorNotFoundError as e:
        assert e.args[0] == "Collector not found"
