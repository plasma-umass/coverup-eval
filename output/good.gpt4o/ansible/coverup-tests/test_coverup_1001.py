# file lib/ansible/parsing/yaml/dumper.py:33-37
# lines [33, 34]
# branches []

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
from yaml import dump, SafeDumper

def test_ansible_dumper():
    class CustomType:
        def __init__(self, value):
            self.value = value

    def custom_representer(dumper, data):
        return dumper.represent_scalar('!custom', data.value)

    AnsibleDumper.add_representer(CustomType, custom_representer)

    obj = CustomType('test_value')
    yaml_str = dump(obj, Dumper=AnsibleDumper)

    assert yaml_str == '!custom test_value\n'

    # Clean up by removing the custom representer
    AnsibleDumper.yaml_representers.pop(CustomType, None)
