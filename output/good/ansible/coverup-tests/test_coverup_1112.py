# file lib/ansible/parsing/yaml/dumper.py:57-61
# lines [57, 61]
# branches []

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
from jinja2.runtime import Undefined
from yaml.representer import RepresenterError

class TestAnsibleDumper:

    def test_represent_undefined(self):
        dumper = AnsibleDumper(None)
        undefined_data = Undefined()

        # Expect the test to raise a RepresenterError due to the undefined data
        with pytest.raises(RepresenterError) as exc_info:
            dumper.represent_undefined(undefined_data)

        assert "cannot represent an object" in str(exc_info.value), "The exception message should contain 'cannot represent an object'"
