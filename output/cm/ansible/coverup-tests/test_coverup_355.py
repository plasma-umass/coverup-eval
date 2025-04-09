# file lib/ansible/cli/doc.py:867-888
# lines [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888]
# branches []

import pytest
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.module_utils._text import to_native
import traceback

# Mock the Display class to capture the verbose output
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.patch('ansible.cli.doc.display', spec=Display)
    display_mock.vvv = mocker.MagicMock()
    return display_mock

# Test function to cover the exception handling block
def test_format_plugin_doc_exception_handling(mock_display, mocker):
    plugin = "test_plugin"
    plugin_type = "module"
    doc = {'collection': 'test_collection'}
    plainexamples = "examples"
    returndocs = "return_docs"
    metadata = "metadata"

    # Mock the get_man_text method to raise an exception
    mocker.patch.object(DocCLI, 'get_man_text', side_effect=Exception("Test Exception"))

    with pytest.raises(AnsibleError) as excinfo:
        DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert "Unable to retrieve documentation from 'test_plugin'" in str(excinfo.value)
    assert mock_display.vvv.called
    assert "Test Exception" in str(excinfo.value.orig_exc)
