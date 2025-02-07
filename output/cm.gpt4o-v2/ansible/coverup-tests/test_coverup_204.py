# file: lib/ansible/modules/yum_repository.py:554-573
# asked: {"lines": [554, 555, 557, 558, 559, 560, 561, 562, 563, 566, 567, 568, 569, 571, 572, 573], "branches": [[555, 557], [555, 566]]}
# gained: {"lines": [554, 555, 557, 558, 559, 560, 561, 562, 563, 566, 567, 568, 569, 571, 572, 573], "branches": [[555, 557], [555, 566]]}

import os
import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.module_utils._text import to_native
from ansible.module_utils.six.moves import configparser
from ansible.modules.yum_repository import YumRepo

@pytest.fixture
def module():
    return MagicMock()

@pytest.fixture
def yum_repo(module):
    module.params = {
        'repoid': 'testrepo',
        'reposdir': '/tmp',
        'file': 'testfile',
        'dest': '/tmp/testfile.repo'
    }
    return YumRepo(module)

def test_save_with_sections(yum_repo, module):
    yum_repo.repofile = configparser.RawConfigParser()
    yum_repo.repofile.add_section('testsection')
    
    with patch('builtins.open', mock_open()) as mocked_file:
        with patch.object(yum_repo.repofile, 'write', wraps=yum_repo.repofile.write) as mocked_write:
            yum_repo.save()
            mocked_file.assert_called_once_with('/tmp/testfile.repo', 'w')
            mocked_write.assert_called_once()

def test_save_with_ioerror(yum_repo, module):
    yum_repo.repofile = configparser.RawConfigParser()
    yum_repo.repofile.add_section('testsection')
    
    with patch('builtins.open', mock_open()) as mocked_file:
        mocked_file.side_effect = IOError('Test IOError')
        yum_repo.save()
        module.fail_json.assert_called_once_with(
            msg='Problems handling file /tmp/testfile.repo.',
            details=to_native(IOError('Test IOError'))
        )

def test_save_without_sections(yum_repo, module):
    yum_repo.repofile = configparser.RawConfigParser()
    
    with patch('os.remove') as mocked_remove:
        yum_repo.save()
        mocked_remove.assert_called_once_with('/tmp/testfile.repo')

def test_save_with_oserror(yum_repo, module):
    yum_repo.repofile = configparser.RawConfigParser()
    
    with patch('os.remove') as mocked_remove:
        mocked_remove.side_effect = OSError('Test OSError')
        yum_repo.save()
        module.fail_json.assert_called_once_with(
            msg='Cannot remove empty repo file /tmp/testfile.repo.',
            details=to_native(OSError('Test OSError'))
        )
