# file lib/ansible/modules/yum_repository.py:554-573
# lines [554, 555, 557, 558, 559, 560, 561, 562, 563, 566, 567, 568, 569, 571, 572, 573]
# branches ['555->557', '555->566']

import os
import pytest
from unittest import mock
from ansible.modules.yum_repository import YumRepo

@pytest.fixture
def yum_repo():
    class MockModule:
        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

    class MockRepoFile:
        def __init__(self, sections):
            self._sections = sections

        def sections(self):
            return self._sections

        def write(self, fd):
            fd.write("[mock]\nname=Mock Repo\nbaseurl=http://mock.repo.url\n")

    mock_module = MockModule()
    mock_repofile = MockRepoFile([])
    
    class TestYumRepo(YumRepo):
        def __init__(self, module, repofile):
            self.module = module
            self.repofile = repofile
            self.params = {}

    return TestYumRepo(mock_module, mock_repofile)

def test_yum_repo_save_with_sections(yum_repo, tmpdir):
    yum_repo.params = {'dest': str(tmpdir.join('yum.repo'))}
    yum_repo.repofile.sections = mock.Mock(return_value=['mock_section'])

    yum_repo.save()

    with open(yum_repo.params['dest'], 'r') as f:
        content = f.read()
    assert "[mock]\nname=Mock Repo\nbaseurl=http://mock.repo.url\n" in content

def test_yum_repo_save_without_sections(yum_repo, tmpdir):
    yum_repo.params = {'dest': str(tmpdir.join('yum.repo'))}
    yum_repo.repofile.sections = mock.Mock(return_value=[])

    with open(yum_repo.params['dest'], 'w') as f:
        f.write("dummy content")

    yum_repo.save()

    assert not os.path.exists(yum_repo.params['dest'])

def test_yum_repo_save_ioerror(yum_repo, tmpdir):
    yum_repo.params = {'dest': '/nonexistent/yum.repo'}
    yum_repo.repofile.sections = mock.Mock(return_value=['mock_section'])

    with pytest.raises(Exception) as excinfo:
        yum_repo.save()
    assert "Problems handling file /nonexistent/yum.repo." in str(excinfo.value)

def test_yum_repo_save_oserror(yum_repo, tmpdir):
    yum_repo.params = {'dest': '/nonexistent/yum.repo'}
    yum_repo.repofile.sections = mock.Mock(return_value=[])

    with pytest.raises(Exception) as excinfo:
        yum_repo.save()
    assert "Cannot remove empty repo file /nonexistent/yum.repo." in str(excinfo.value)
