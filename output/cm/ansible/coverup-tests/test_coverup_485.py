# file lib/ansible/executor/discovery/python_target.py:16-22
# lines [16, 17, 18, 19, 20, 22]
# branches ['17->18', '17->19']

import os
import pytest
from ansible.executor.discovery.python_target import read_utf8_file

def test_read_utf8_file(tmp_path, mocker):
    # Create a temporary file with some content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    test_file.write_text(test_content, encoding='utf-8')

    # Test that the content is read correctly
    assert read_utf8_file(str(test_file)) == test_content

    # Test that None is returned if the file is not readable
    mocker.patch('os.access', return_value=False)
    assert read_utf8_file(str(test_file)) is None

    # Cleanup is handled by pytest's tmp_path fixture automatically
