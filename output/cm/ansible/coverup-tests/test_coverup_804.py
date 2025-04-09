# file lib/ansible/module_utils/facts/system/selinux.py:36-39
# lines [36, 37, 38]
# branches []

import pytest
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

# Since the provided code snippet is just a class definition with no methods,
# we need to create a test that checks the instantiation of the class and its attributes.

def test_selinux_fact_collector_instantiation(mocker):
    # Mocking the BaseFactCollector to avoid any side effects
    mocker.patch('ansible.module_utils.facts.system.selinux.BaseFactCollector')

    # Instantiate the SelinuxFactCollector
    selinux_collector = SelinuxFactCollector()

    # Assertions to verify the instantiation and attributes
    assert selinux_collector.name == 'selinux'
    assert selinux_collector._fact_ids == set()

    # Clean up is not necessary as we are mocking the base class and not creating any external resources
