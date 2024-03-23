# file lib/ansible/utils/_junit_xml.py:172-186
# lines [172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185]
# branches []

import dataclasses
import datetime
import pytest
from ansible.utils._junit_xml import TestSuite

@pytest.fixture
def test_suite():
    # Assuming the TestSuite class has a different set of fields
    # and does not have 'disabled', 'errors', 'failures', 'hostname', 'id', 'package', 'skipped', 'tests', 'time'
    # Adjust the fixture to only use the fields that are actually present in the TestSuite class
    return TestSuite(
        name="test_suite",
        timestamp=datetime.datetime.now(),
    )

def test_get_attributes(test_suite):
    attributes = test_suite.get_attributes()
    assert isinstance(attributes, dict)
    assert 'name' in attributes
    assert attributes['name'] == "test_suite"
    assert 'timestamp' in attributes
    assert attributes['timestamp'] is not None
    assert isinstance(attributes['timestamp'], str)
