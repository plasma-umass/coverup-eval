# file lib/ansible/parsing/splitter.py:49-103
# lines [69]
# branches ['66->69']

import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.splitter import parse_kv

def test_parse_kv_with_unmatched_quote_exception():
    with pytest.raises(AnsibleParserError) as excinfo:
        parse_kv('key="value')
    assert "failed at splitting arguments, either an unbalanced jinja2 block or quotes" in str(excinfo.value)

def test_parse_kv_with_unexpected_exception(mocker):
    mocker.patch('ansible.parsing.splitter.split_args', side_effect=ValueError('unexpected error'))
    with pytest.raises(ValueError) as excinfo:
        parse_kv('key=value')
    assert "unexpected error" in str(excinfo.value)
