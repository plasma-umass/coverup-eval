# file lib/ansible/module_utils/facts/system/local.py:34-104
# lines [34, 35, 36, 38, 39, 41, 43, 44, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 59, 61, 62, 63, 64, 67, 69, 71, 72, 73, 74, 75, 76, 79, 80, 81, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101, 103, 104]
# branches ['38->39', '38->41', '43->44', '43->46', '48->50', '48->103', '51->52', '51->67', '56->57', '56->61', '61->62', '61->69', '91->92', '91->101', '92->93', '92->94', '94->91', '94->95']

import os
import pytest
import json
import stat
import glob
import configparser
from io import StringIO
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.local import LocalFactCollector
from ansible.module_utils._text import to_text
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    module = MagicMock(spec=AnsibleModule)
    module.params = {'fact_path': '/tmp/facts'}
    return module

@pytest.fixture
def setup_fact_files(tmp_path):
    fact_path = tmp_path / "facts"
    fact_path.mkdir()
    
    # Create a .fact file that is executable
    exec_fact_file = fact_path / "exec_fact.fact"
    exec_fact_file.write_text("#!/bin/bash\necho '{\"key\": \"value\"}'")
    exec_fact_file.chmod(exec_fact_file.stat().st_mode | stat.S_IXUSR)
    
    # Create a .fact file that is not executable
    non_exec_fact_file = fact_path / "non_exec_fact.fact"
    non_exec_fact_file.write_text("{\"key\": \"value\"}")
    
    # Create a .fact file with invalid JSON
    invalid_json_fact_file = fact_path / "invalid_json_fact.fact"
    invalid_json_fact_file.write_text("invalid json content")
    
    # Create a .fact file with INI content
    ini_fact_file = fact_path / "ini_fact.fact"
    ini_fact_file.write_text("[section]\noption=value")
    
    return fact_path

def test_collect_local_facts(mock_module, setup_fact_files, mocker):
    fact_path = str(setup_fact_files)
    mock_module.params['fact_path'] = fact_path
    
    def mock_run_command(cmd):
        if "exec_fact.fact" in cmd:
            return (0, '{"key": "value"}', '')
        return (1, '', 'error')
    
    mock_module.run_command.side_effect = mock_run_command
    
    collector = LocalFactCollector()
    
    with patch('glob.glob', return_value=glob.glob(fact_path + '/*.fact')):
        with patch('os.path.exists', return_value=True):
            collected_facts = collector.collect(module=mock_module)
    
    assert 'local' in collected_facts
    local_facts = collected_facts['local']
    
    assert 'exec_fact' in local_facts
    assert local_facts['exec_fact'] == {"key": "value"}
    
    assert 'non_exec_fact' in local_facts
    assert local_facts['non_exec_fact'] == {"key": "value"}
    
    assert 'invalid_json_fact' in local_facts
    assert "error loading facts as JSON or ini" in local_facts['invalid_json_fact']
    
    assert 'ini_fact' in local_facts
    assert 'section' in local_facts['ini_fact']
    assert local_facts['ini_fact']['section']['option'] == 'value'
