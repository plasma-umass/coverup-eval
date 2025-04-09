# file: lib/ansible/module_utils/facts/collector.py:223-236
# asked: {"lines": [223, 224, 225, 227, 228, 230, 232, 233, 234, 236], "branches": [[227, 228], [227, 236], [232, 227], [232, 233]]}
# gained: {"lines": [223, 224, 225, 227, 228, 230, 232, 233, 234, 236], "branches": [[227, 228], [227, 236], [232, 227], [232, 233]]}

import pytest
from collections import defaultdict
from unittest.mock import MagicMock

# Assuming the build_fact_id_to_collector_map function is defined in ansible/module_utils/facts/collector.py
from ansible.module_utils.facts.collector import build_fact_id_to_collector_map

def test_build_fact_id_to_collector_map():
    # Mock collector classes
    collector_class_1 = MagicMock()
    collector_class_1.name = "collector1"
    collector_class_1._fact_ids = ["fact1", "fact2"]

    collector_class_2 = MagicMock()
    collector_class_2.name = "collector2"
    collector_class_2._fact_ids = ["fact3"]

    collectors_for_platform = [collector_class_1, collector_class_2]

    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # Assertions to verify the correctness of the function
    assert fact_id_to_collector_map["collector1"] == [collector_class_1]
    assert fact_id_to_collector_map["collector2"] == [collector_class_2]
    assert fact_id_to_collector_map["fact1"] == [collector_class_1]
    assert fact_id_to_collector_map["fact2"] == [collector_class_1]
    assert fact_id_to_collector_map["fact3"] == [collector_class_2]

    assert aliases_map["collector1"] == {"fact1", "fact2"}
    assert aliases_map["collector2"] == {"fact3"}

    # Clean up
    del collector_class_1
    del collector_class_2
    del collectors_for_platform
    del fact_id_to_collector_map
    del aliases_map
