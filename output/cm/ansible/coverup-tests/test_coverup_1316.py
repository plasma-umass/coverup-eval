# file lib/ansible/modules/subversion.py:198-204
# lines [200, 201, 202, 203, 204]
# branches ['201->202', '201->203']

import pytest
from unittest.mock import MagicMock

# Assuming the Subversion class is part of the module ansible.modules.subversion
from ansible.modules.subversion import Subversion

@pytest.fixture
def svn_instance(mocker):
    # Mock the _exec method to prevent actual execution
    mocker.patch.object(Subversion, '_exec')
    # Create a Subversion instance with the required arguments mocked
    svn = Subversion(
        module=MagicMock(),
        dest='/path/to/checkout',
        repo='http://example.com/repo',
        revision='HEAD',
        username=None,
        password=None,
        svn_path=None,
        validate_certs=True
    )
    return svn

def test_checkout_with_force(svn_instance):
    # Call the checkout method with force=True
    svn_instance.checkout(force=True)
    # Assert that _exec was called with the correct command
    svn_instance._exec.assert_called_once_with(['checkout', '--force', '-r', svn_instance.revision, svn_instance.repo, svn_instance.dest])

def test_checkout_without_force(svn_instance):
    # Call the checkout method with force=False
    svn_instance.checkout(force=False)
    # Assert that _exec was called with the correct command
    svn_instance._exec.assert_called_once_with(['checkout', '-r', svn_instance.revision, svn_instance.repo, svn_instance.dest])
