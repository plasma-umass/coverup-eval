# file lib/ansible/parsing/utils/yaml.py:25-43
# lines [34, 35, 36, 37, 39, 40, 41, 43]
# branches ['35->36', '35->39']

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.utils.yaml import _handle_error, AnsibleParserError

def test_handle_error_with_problem_mark():
    json_exc = Mock()
    yaml_exc = Mock()
    yaml_exc.problem_mark = Mock()
    yaml_exc.problem_mark.line = 10
    yaml_exc.problem_mark.column = 5
    yaml_exc.problem = "some problem"
    file_name = "test_file.yml"
    show_content = True

    with patch('ansible.parsing.utils.yaml.AnsibleBaseYAMLObject') as MockAnsibleBaseYAMLObject, \
         patch('ansible.parsing.utils.yaml.to_native', side_effect=lambda x: x), \
         patch('ansible.parsing.utils.yaml.YAML_SYNTAX_ERROR', "%s"):
        
        mock_err_obj = MockAnsibleBaseYAMLObject.return_value
        with pytest.raises(AnsibleParserError) as exc_info:
            _handle_error(json_exc, yaml_exc, file_name, show_content)
        
        assert exc_info.value.obj == mock_err_obj
        assert exc_info.value.obj.ansible_pos == (file_name, 11, 6)
        assert exc_info.value._show_content == show_content
        assert exc_info.value.orig_exc == yaml_exc
        assert "some problem" in str(exc_info.value)
