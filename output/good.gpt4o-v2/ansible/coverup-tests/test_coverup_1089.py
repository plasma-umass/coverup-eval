# file: lib/ansible/parsing/splitter.py:155-286
# asked: {"lines": [207, 208, 214, 215, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 252, 253, 258, 259, 264, 265, 276, 284], "branches": [[206, 207], [213, 214], [232, 233], [235, 236], [236, 237], [236, 238], [238, 239], [238, 244], [240, 241], [240, 242], [251, 252], [257, 258], [263, 264], [275, 276], [283, 284]]}
# gained: {"lines": [207, 208, 214, 215, 233, 234, 236, 238, 239, 240, 241, 242, 245, 252, 253, 276, 284], "branches": [[206, 207], [213, 214], [232, 233], [235, 236], [236, 238], [238, 239], [240, 241], [251, 252], [275, 276], [283, 284]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.splitter import split_args

def test_split_args_empty_token():
    args = 'a=b  c=d'
    result = split_args(args)
    assert result == ['a=b ', 'c=d']

def test_split_args_line_continuation():
    args = 'a=b \\\nc=d'
    result = split_args(args)
    assert result == ['a=b', 'c=d']

def test_split_args_inside_quotes():
    args = 'a="b c" d=e'
    result = split_args(args)
    assert result == ['a="b c"', 'd=e']

def test_split_args_jinja2_blocks():
    args = '{{ a }} b={{ c }}'
    result = split_args(args)
    assert result == ['{{ a }}', 'b={{ c }}']

def test_split_args_unbalanced_jinja2_blocks():
    args = '{{ a b={{ c }}'
    with pytest.raises(AnsibleParserError):
        split_args(args)

def test_split_args_unbalanced_quotes():
    args = 'a="b c d=e'
    with pytest.raises(AnsibleParserError):
        split_args(args)

def test_split_args_multiline():
    args = 'a=b\nc=d'
    result = split_args(args)
    assert result == ['a=b\n', 'c=d']

def test_split_args_multiline_with_continuation():
    args = 'a=b \\\nc=d'
    result = split_args(args)
    assert result == ['a=b', 'c=d']
