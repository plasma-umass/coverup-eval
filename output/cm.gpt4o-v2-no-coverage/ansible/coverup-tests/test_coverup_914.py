# file: lib/ansible/plugins/filter/core.py:66-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

import pytest
import json
from ansible.parsing.ajson import AnsibleJSONEncoder
from ansible.plugins.filter.core import to_json

def test_to_json_basic():
    data = {"key": "value"}
    result = to_json(data)
    assert result == json.dumps(data, cls=AnsibleJSONEncoder)

def test_to_json_with_args():
    data = {"key": "value"}
    result = to_json(data, indent=4)
    assert result == json.dumps(data, cls=AnsibleJSONEncoder, indent=4)

def test_to_json_with_kwargs():
    data = {"key": "value"}
    result = to_json(data, separators=(',', ':'))
    assert result == json.dumps(data, cls=AnsibleJSONEncoder, separators=(',', ':'))

def test_to_json_with_args_and_kwargs():
    data = {"key": "value"}
    result = to_json(data, indent=4, separators=(',', ':'))
    assert result == json.dumps(data, cls=AnsibleJSONEncoder, indent=4, separators=(',', ':'))
