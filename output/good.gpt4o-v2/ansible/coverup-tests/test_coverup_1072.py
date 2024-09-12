# file: lib/ansible/parsing/yaml/dumper.py:33-37
# asked: {"lines": [33, 34], "branches": []}
# gained: {"lines": [33, 34], "branches": []}

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.module_utils.common.yaml import SafeDumper

def test_ansible_dumper_inheritance():
    # Verify that AnsibleDumper is a subclass of SafeDumper
    assert issubclass(AnsibleDumper, SafeDumper)

def test_ansible_dumper_docstring():
    # Verify that the docstring is correctly set
    expected_docstring = """
    A simple stub class that allows us to add representers
    for our overridden object types.
    """.strip()
    assert AnsibleDumper.__doc__.strip() == expected_docstring
