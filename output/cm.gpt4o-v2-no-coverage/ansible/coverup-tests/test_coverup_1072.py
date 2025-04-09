# file: lib/ansible/parsing/yaml/dumper.py:33-37
# asked: {"lines": [33, 34], "branches": []}
# gained: {"lines": [33, 34], "branches": []}

import pytest
from ansible.module_utils.common.yaml import SafeDumper
from ansible.parsing.yaml.dumper import AnsibleDumper

def test_ansible_dumper_inheritance():
    assert issubclass(AnsibleDumper, SafeDumper), "AnsibleDumper should inherit from SafeDumper"

def test_ansible_dumper_docstring():
    expected_docstring = """
    A simple stub class that allows us to add representers
    for our overridden object types.
    """.strip()
    assert AnsibleDumper.__doc__.strip() == expected_docstring, "Docstring does not match"
