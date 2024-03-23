# file lib/ansible/module_utils/facts/other/facter.py:26-29
# lines [26, 27, 28]
# branches []

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector

# Assuming the FacterFactCollector class is part of a larger file and has more code that we don't see here.
# The test below is designed to create an instance of the class and check its attributes.

def test_facter_fact_collector():
    facter_collector = FacterFactCollector()
    assert facter_collector.name == 'facter'
    assert facter_collector._fact_ids == set(['facter'])
