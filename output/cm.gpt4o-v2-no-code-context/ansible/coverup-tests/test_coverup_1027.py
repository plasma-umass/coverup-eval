# file: lib/ansible/module_utils/facts/system/distribution.py:154-165
# asked: {"lines": [156, 157, 158, 159, 161, 164, 165], "branches": []}
# gained: {"lines": [156, 157, 158, 159, 161, 164, 165], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DistributionFiles class is defined in a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    # Mocking the 'module' argument required by DistributionFiles
    module_mock = MagicMock()
    return DistributionFiles(module=module_mock)

def test_guess_distribution_all_none(monkeypatch, distribution_files):
    def mock_get_distribution():
        return None

    def mock_get_distribution_version():
        return None

    def mock_get_distribution_codename():
        return None

    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution', mock_get_distribution)
    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution_version', mock_get_distribution_version)
    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution_codename', mock_get_distribution_codename)

    result = distribution_files._guess_distribution()
    assert result == {
        'distribution': 'NA',
        'distribution_version': 'NA',
        'distribution_release': 'NA',
        'distribution_major_version': 'NA'
    }

def test_guess_distribution_partial(monkeypatch, distribution_files):
    def mock_get_distribution():
        return 'Ubuntu'

    def mock_get_distribution_version():
        return None

    def mock_get_distribution_codename():
        return 'focal'

    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution', mock_get_distribution)
    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution_version', mock_get_distribution_version)
    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution_codename', mock_get_distribution_codename)

    result = distribution_files._guess_distribution()
    assert result == {
        'distribution': 'Ubuntu',
        'distribution_version': 'NA',
        'distribution_release': 'focal',
        'distribution_major_version': 'NA'
    }

def test_guess_distribution_full(monkeypatch, distribution_files):
    def mock_get_distribution():
        return 'Ubuntu'

    def mock_get_distribution_version():
        return '20.04'

    def mock_get_distribution_codename():
        return 'focal'

    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution', mock_get_distribution)
    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution_version', mock_get_distribution_version)
    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.get_distribution_codename', mock_get_distribution_codename)

    result = distribution_files._guess_distribution()
    assert result == {
        'distribution': 'Ubuntu',
        'distribution_version': '20.04',
        'distribution_release': 'focal',
        'distribution_major_version': '20'
    }
