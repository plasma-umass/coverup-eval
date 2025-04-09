# file lib/ansible/module_utils/facts/collector.py:54-55
# lines [54, 55]
# branches []

import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

def test_collector_not_found_error():
    with pytest.raises(CollectorNotFoundError) as excinfo:
        raise CollectorNotFoundError("Collector not found")
    assert excinfo.value.args[0] == "Collector not found"
