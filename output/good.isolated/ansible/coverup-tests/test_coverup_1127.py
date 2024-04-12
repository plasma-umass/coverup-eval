# file lib/ansible/module_utils/facts/system/local.py:34-104
# lines [35, 36, 38, 39, 41, 43, 44, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 59, 61, 62, 63, 64, 67, 69, 71, 72, 73, 74, 75, 76, 79, 80, 81, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101, 103, 104]
# branches ['38->39', '38->41', '43->44', '43->46', '48->50', '48->103', '51->52', '51->67', '56->57', '56->61', '61->62', '61->69', '91->92', '91->101', '92->93', '92->94', '94->91', '94->95']

import json
import os
import pytest
import stat
import tempfile
from unittest.mock import MagicMock

# Assuming the LocalFactCollector class is imported from the appropriate module
from ansible.module_utils.facts.system.local import LocalFactCollector

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.params = {"fact_path": None}
    mock_module.run_command = MagicMock()
    mocker.patch('os.path.exists', return_value=True)
    return mock_module

@pytest.fixture
def fact_dir():
    new_dir = tempfile.mkdtemp()
    yield new_dir
    os.rmdir(new_dir)

def test_local_fact_collector(mock_module, fact_dir):
    mock_module.params['fact_path'] = fact_dir

    # Create a fake .fact file
    fact_file = os.path.join(fact_dir, 'test.fact')
    with open(fact_file, 'w') as f:
        f.write(json.dumps({"key": "value"}))

    # Set the file as executable
    st = os.stat(fact_file)
    os.chmod(fact_file, st.st_mode | stat.S_IXUSR)

    # Mock the run_command to simulate script execution
    mock_module.run_command.return_value = (0, '{"executed_key": "executed_value"}', '')

    # Create the LocalFactCollector instance and collect facts
    collector = LocalFactCollector()
    facts = collector.collect(module=mock_module)

    # Assertions to ensure the facts were collected correctly
    assert 'local' in facts
    assert 'test' in facts['local']
    assert facts['local']['test'] == {"executed_key": "executed_value"}

    # Clean up the created .fact file
    os.remove(fact_file)
