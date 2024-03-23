# file lib/ansible/module_utils/facts/system/distribution.py:460-467
# lines [460, 461, 463, 464, 465, 467]
# branches ['463->464', '463->467']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_collected_facts():
    return {}

@pytest.fixture
def distribution_files():
    mock_module = MagicMock()
    return DistributionFiles(module=mock_module)

def test_parse_distribution_file_centos_stream(distribution_files, mock_collected_facts, tmp_path):
    # Create a temporary file to simulate the CentOS Stream distribution file
    fake_path = tmp_path / "centos_stream"
    fake_path.write_text("CentOS Stream release 8")

    # Call the method under test
    result, centos_facts = distribution_files.parse_distribution_file_CentOS(
        name="CentOS",
        data=fake_path.read_text(),
        path=str(fake_path),
        collected_facts=mock_collected_facts
    )

    # Assert that the method recognizes CentOS Stream
    assert result is True
    assert centos_facts['distribution_release'] == 'Stream'

def test_parse_distribution_file_centos(distribution_files, mock_collected_facts, tmp_path):
    # Create a temporary file to simulate a non-Stream CentOS distribution file
    fake_path = tmp_path / "centos"
    fake_path.write_text("CentOS release 7.9.2009 (Core)")

    # Call the method under test
    result, centos_facts = distribution_files.parse_distribution_file_CentOS(
        name="CentOS",
        data=fake_path.read_text(),
        path=str(fake_path),
        collected_facts=mock_collected_facts
    )

    # Assert that the method does not recognize CentOS Stream
    assert result is False
    assert 'distribution_release' not in centos_facts
