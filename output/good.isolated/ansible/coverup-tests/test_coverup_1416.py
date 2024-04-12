# file lib/ansible/module_utils/facts/packages.py:53-69
# lines [59, 60]
# branches []

import pytest
from ansible.module_utils.facts.packages import LibMgr

class MockLibMgr(LibMgr):
    LIB = "os"

    def get_package_details(self):
        pass

    def list_installed(self):
        pass

@pytest.fixture
def mock_libmgr():
    return MockLibMgr()

def test_libmgr_initialization(mock_libmgr):
    assert mock_libmgr._lib is None
    assert isinstance(mock_libmgr, LibMgr)
