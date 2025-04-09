# file lib/ansible/parsing/splitter.py:155-286
# lines [207, 208, 214, 215, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 252, 253, 258, 259, 264, 265, 276, 284]
# branches ['206->207', '213->214', '232->233', '235->236', '236->237', '236->238', '238->239', '238->244', '240->241', '240->242', '251->252', '257->258', '263->264', '275->276', '283->284']

import pytest
from ansible.parsing.splitter import split_args, AnsibleParserError

def _get_quote_state(token, quote_char):
    if quote_char:
        if token.endswith(quote_char):
            return None
        return quote_char
    if token.startswith('"') or token.startswith("'"):
        return token[0]
    return None

def _count_jinja2_blocks(token, depth, start, end):
    depth += token.count(start)
    depth -= token.count(end)
    return depth

def test_split_args_unbalanced_quotes():
    with pytest.raises(AnsibleParserError):
        split_args('a="unbalanced quote')

def test_split_args_unbalanced_jinja2():
    with pytest.raises(AnsibleParserError):
        split_args('a={{ unbalanced jinja2')

def test_split_args_line_continuation():
    result = split_args('a=1 \\\nb=2')
    assert result == ['a=1', 'b=2']

def test_split_args_empty_token():
    result = split_args('a=1  b=2')
    assert result == ['a=1 ', 'b=2']

def test_split_args_nested_jinja2():
    result = split_args('a={{ foo }} b={% bar %} c={# baz #}')
    assert result == ['a={{ foo }}', 'b={% bar %}', 'c={# baz #}']

def test_split_args_multiline():
    result = split_args('a=1\nb=2\nc=3')
    assert result == ['a=1\n', 'b=2\n', 'c=3']

def test_split_args_complex():
    result = split_args('a={{ foo }} b="bar baz" c={% if true %} d={# comment #}')
    assert result == ['a={{ foo }}', 'b="bar baz"', 'c={% if true %}', 'd={# comment #}']
