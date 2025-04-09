# file lib/ansible/cli/doc.py:890-936
# lines [894, 896, 898, 899, 900, 902, 903, 904, 906, 907, 908, 909, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 925, 926, 928, 930, 931, 933, 934, 936]
# branches ['898->899', '898->902', '902->903', '902->906', '907->908', '907->936', '911->912', '911->913', '913->914', '913->915', '915->916', '915->917', '917->918', '917->919', '919->920', '919->921', '921->922', '921->925', '922->923', '922->925', '928->907', '928->930', '930->931', '930->933']

import os
import pytest
from unittest import mock
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.doc.display', autospec=True)

@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.cli.doc.C.REJECT_EXTS', ['.rej'])
    mocker.patch('ansible.cli.doc.C.IGNORE_FILES', ['ignore_me'])
    mocker.patch('ansible.cli.doc.REJECTLIST', {'PLUGIN': ['rejected_plugin']})

def test_find_plugins(mock_display, mock_constants, tmp_path):
    # Create a temporary directory and files for testing
    test_dir = tmp_path / "test_plugins"
    test_dir.mkdir()
    
    # Create some test files
    (test_dir / "valid_plugin.py").write_text("print('valid')")
    (test_dir / "ignore_me").write_text("print('ignore')")
    (test_dir / "rejected_plugin.py").write_text("print('rejected')")
    (test_dir / ".hidden_plugin.py").write_text("print('hidden')")
    (test_dir / "_deprecated_plugin.py").write_text("print('deprecated')")
    (test_dir / "valid_plugin.rej").write_text("print('rejected_ext')")
    
    # Test with a valid directory
    plugins = DocCLI.find_plugins(str(test_dir), internal=True, ptype='plugin')
    assert "valid_plugin" in plugins
    assert "deprecated_plugin" in plugins
    assert "ignore_me" not in plugins
    assert "rejected_plugin" not in plugins
    assert ".hidden_plugin" not in plugins
    assert "valid_plugin.rej" not in plugins
    
    # Test with a non-existent path
    plugins = DocCLI.find_plugins(str(test_dir / "non_existent"), internal=True, ptype='plugin')
    assert plugins == set()
    
    # Test with a path that is not a directory
    non_dir_file = test_dir / "not_a_directory"
    non_dir_file.write_text("not a directory")
    plugins = DocCLI.find_plugins(str(non_dir_file), internal=True, ptype='plugin')
    assert plugins == set()
    
    # Verify display calls
    mock_display.vvvv.assert_any_call("Searching %s for plugins" % str(test_dir))
    mock_display.vvvv.assert_any_call("Found valid_plugin.py")
    mock_display.vvvv.assert_any_call("Added valid_plugin")
    mock_display.vvvv.assert_any_call("Found _deprecated_plugin.py")
    mock_display.vvvv.assert_any_call("Added deprecated_plugin")
    mock_display.vvvv.assert_any_call("Found ignore_me")
    mock_display.vvvv.assert_any_call("Found rejected_plugin.py")
    mock_display.vvvv.assert_any_call("Found .hidden_plugin.py")
    mock_display.vvvv.assert_any_call("Found valid_plugin.rej")
    mock_display.vvvv.assert_any_call("%s does not exist" % str(test_dir / "non_existent"))
    mock_display.vvvv.assert_any_call("%s is not a directory" % str(non_dir_file))
