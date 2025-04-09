# file: lib/ansible/parsing/yaml/dumper.py:33-37
# asked: {"lines": [33, 34], "branches": []}
# gained: {"lines": [33, 34], "branches": []}

import pytest
from ansible.parsing.yaml.dumper import SafeDumper

def test_ansible_dumper_class():
    class AnsibleDumper(SafeDumper):
        '''
        A simple stub class that allows us to add representers
        for our overridden object types.
        '''
    assert issubclass(AnsibleDumper, SafeDumper)
