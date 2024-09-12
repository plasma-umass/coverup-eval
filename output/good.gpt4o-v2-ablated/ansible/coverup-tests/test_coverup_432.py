# file: lib/ansible/parsing/utils/yaml.py:25-43
# asked: {"lines": [34, 35, 36, 37, 39, 40, 41, 43], "branches": [[35, 36], [35, 39]]}
# gained: {"lines": [34, 35, 36, 37, 39, 40, 41, 43], "branches": [[35, 36], [35, 39]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the following imports are available from the ansible codebase
from ansible.errors import AnsibleParserError
from ansible.parsing.utils.yaml import _handle_error, AnsibleBaseYAMLObject, YAML_SYNTAX_ERROR
from ansible.module_utils._text import to_native

def test_handle_error_with_problem_mark():
    json_exc = Mock()
    yaml_exc = Mock()
    yaml_exc.problem_mark = Mock(line=10, column=5)
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with pytest.raises(AnsibleParserError) as exc_info:
        _handle_error(json_exc, yaml_exc, file_name, show_content)

    assert isinstance(exc_info.value, AnsibleParserError)
    assert exc_info.value.obj.ansible_pos == (file_name, 11, 6)
    assert "some problem" in str(exc_info.value)
    assert "JSON:" in str(exc_info.value)

def test_handle_error_without_problem_mark():
    json_exc = Mock()
    yaml_exc = Mock()
    del yaml_exc.problem_mark
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with pytest.raises(AnsibleParserError) as exc_info:
        _handle_error(json_exc, yaml_exc, file_name, show_content)

    assert isinstance(exc_info.value, AnsibleParserError)
    assert exc_info.value.obj is None
    assert "some problem" in str(exc_info.value)
    assert "JSON:" in str(exc_info.value)
