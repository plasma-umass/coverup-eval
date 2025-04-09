# file: lib/ansible/utils/_junit_xml.py:238-247
# asked: {"lines": [238, 240, 241, 242, 243, 244, 245, 246], "branches": []}
# gained: {"lines": [238, 240, 241, 242, 243, 244, 245, 246], "branches": []}

import pytest
from unittest.mock import MagicMock
import decimal
from ansible.utils._junit_xml import TestSuites, _attributes

@pytest.fixture
def test_suites():
    return TestSuites(
        name="Sample Test Suite",
        suites=[]
    )

def test_get_attributes(test_suites, mocker):
    mocker.patch.object(TestSuites, 'disabled', new_callable=mocker.PropertyMock, return_value=1)
    mocker.patch.object(TestSuites, 'errors', new_callable=mocker.PropertyMock, return_value=2)
    mocker.patch.object(TestSuites, 'failures', new_callable=mocker.PropertyMock, return_value=3)
    mocker.patch.object(TestSuites, 'tests', new_callable=mocker.PropertyMock, return_value=4)
    mocker.patch.object(TestSuites, 'time', new_callable=mocker.PropertyMock, return_value=decimal.Decimal('5.0'))

    attributes = test_suites.get_attributes()

    expected_attributes = {
        'disabled': '1',
        'errors': '2',
        'failures': '3',
        'name': 'Sample Test Suite',
        'tests': '4',
        'time': '5.0'
    }

    assert attributes == expected_attributes
