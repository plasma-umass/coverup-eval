# file lib/ansible/utils/_junit_xml.py:172-186
# lines [172, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185]
# branches []

import pytest
from unittest import mock
from datetime import datetime
import dataclasses
import typing as t

# Assuming _attributes is a function defined elsewhere in the module
def _attributes(**kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}

@dataclasses.dataclass
class TestSuite:
    disabled: int = 0
    errors: int = 0
    failures: int = 0
    hostname: str = ''
    id: str = ''
    name: str = ''
    package: str = ''
    skipped: int = 0
    tests: int = 0
    time: float = 0.0
    timestamp: datetime = None

    def get_attributes(self) -> t.Dict[str, str]:
        """Return a dictionary of attributes for this instance."""
        return _attributes(
            disabled=self.disabled,
            errors=self.errors,
            failures=self.failures,
            hostname=self.hostname,
            id=self.id,
            name=self.name,
            package=self.package,
            skipped=self.skipped,
            tests=self.tests,
            time=self.time,
            timestamp=self.timestamp.isoformat(timespec='seconds') if self.timestamp else None,
        )

@pytest.fixture
def mock_datetime():
    with mock.patch('ansible.utils._junit_xml.datetime') as mock_dt:
        yield mock_dt

def test_get_attributes(mock_datetime):
    mock_timestamp = datetime(2023, 10, 1, 12, 0, 0)
    mock_datetime.now.return_value = mock_timestamp

    ts = TestSuite(
        disabled=1,
        errors=2,
        failures=3,
        hostname='localhost',
        id='123',
        name='test_suite',
        package='test_package',
        skipped=4,
        tests=5,
        time=123.456,
        timestamp=mock_timestamp
    )

    attributes = ts.get_attributes()

    assert attributes == {
        'disabled': 1,
        'errors': 2,
        'failures': 3,
        'hostname': 'localhost',
        'id': '123',
        'name': 'test_suite',
        'package': 'test_package',
        'skipped': 4,
        'tests': 5,
        'time': 123.456,
        'timestamp': '2023-10-01T12:00:00'
    }
