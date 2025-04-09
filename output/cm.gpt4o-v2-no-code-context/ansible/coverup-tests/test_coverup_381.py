# file: lib/ansible/parsing/utils/yaml.py:25-43
# asked: {"lines": [25, 34, 35, 36, 37, 39, 40, 41, 43], "branches": [[35, 36], [35, 39]]}
# gained: {"lines": [25, 34, 35, 36, 37, 39, 40, 41, 43], "branches": [[35, 36], [35, 39]]}

import pytest
from unittest.mock import Mock, patch

# Assuming AnsibleBaseYAMLObject, AnsibleParserError, YAML_SYNTAX_ERROR, and to_native are imported from the appropriate module
from ansible.parsing.utils.yaml import AnsibleBaseYAMLObject, AnsibleParserError, YAML_SYNTAX_ERROR, to_native

# Import the function to be tested
from ansible.parsing.utils.yaml import _handle_error

def test_handle_error_with_problem_mark():
    json_exc = Mock()
    yaml_exc = Mock()
    yaml_exc.problem_mark = Mock(line=10, column=5)
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with pytest.raises(AnsibleParserError) as exc_info:
        _handle_error(json_exc, yaml_exc, file_name, show_content)

    assert exc_info.value.obj.ansible_pos == (file_name, 11, 6)
    assert "some problem" in str(exc_info.value)
    assert exc_info.value._show_content == show_content
    assert exc_info.value.orig_exc == yaml_exc

def test_handle_error_without_problem_mark():
    json_exc = Mock()
    yaml_exc = Mock()
    del yaml_exc.problem_mark
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with pytest.raises(AnsibleParserError) as exc_info:
        _handle_error(json_exc, yaml_exc, file_name, show_content)

    assert exc_info.value.obj is None
    assert "some problem" in str(exc_info.value)
    assert exc_info.value._show_content == show_content
    assert exc_info.value.orig_exc == yaml_exc

@patch('ansible.parsing.utils.yaml.to_native', side_effect=lambda x: x)
def test_handle_error_json_exception(mock_to_native):
    json_exc = Mock()
    yaml_exc = Mock()
    yaml_exc.problem_mark = Mock(line=10, column=5)
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with pytest.raises(AnsibleParserError) as exc_info:
        _handle_error(json_exc, yaml_exc, file_name, show_content)

    assert "JSON: %s" % json_exc in str(exc_info.value)
    assert "some problem" in str(exc_info.value)
    assert exc_info.value._show_content == show_content
    assert exc_info.value.orig_exc == yaml_exc
