# file: lib/ansible/modules/dnf.py:672-687
# asked: {"lines": [674, 675, 678, 679, 680, 681, 684, 685, 686, 687], "branches": [[678, 679], [678, 684], [679, 678], [679, 680], [680, 678], [680, 681], [684, 0], [684, 685], [685, 684], [685, 686], [686, 684], [686, 687]]}
# gained: {"lines": [674, 675, 678, 679, 680, 681, 684, 685, 686, 687], "branches": [[678, 679], [678, 684], [679, 680], [680, 678], [680, 681], [684, 0], [684, 685], [685, 686], [686, 684], [686, 687]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def dnf_module(mocker):
    from ansible.modules.dnf import DnfModule
    module_mock = mocker.MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/locale'
    module_mock.run_command.return_value = (0, 'C.utf8\nen_US.utf8\nC\nPOSIX\n', '')
    return DnfModule(module_mock)

def test_specify_repositories(dnf_module, mocker):
    base = mocker.MagicMock()
    repos = mocker.MagicMock()
    base.repos = repos

    disablerepo = ['repo1', 'repo2']
    enablerepo = ['repo3', 'repo4']

    repo1 = mocker.MagicMock()
    repo2 = mocker.MagicMock()
    repo3 = mocker.MagicMock()
    repo4 = mocker.MagicMock()

    repos.get_matching.side_effect = lambda pattern: {
        'repo1': [repo1],
        'repo2': [repo2],
        'repo3': [repo3],
        'repo4': [repo4]
    }.get(pattern, [])

    dnf_module._specify_repositories(base, disablerepo, enablerepo)

    base.read_all_repos.assert_called_once()

    repo1.disable.assert_called_once()
    repo2.disable.assert_called_once()
    repo3.enable.assert_called_once()
    repo4.enable.assert_called_once()
