# file: lib/ansible/playbook/included_file.py:47-51
# asked: {"lines": [47, 48, 49, 50, 51], "branches": [[48, 49], [48, 51]]}
# gained: {"lines": [47, 48, 49, 50, 51], "branches": [[48, 49], [48, 51]]}

import pytest
from ansible.playbook.included_file import IncludedFile

def test_add_host_new_host():
    included_file = IncludedFile(filename="test.yml", args={}, vars={}, task={})
    included_file.add_host("new_host")
    assert "new_host" in included_file._hosts

def test_add_host_existing_host():
    included_file = IncludedFile(filename="test.yml", args={}, vars={}, task={})
    included_file.add_host("existing_host")
    with pytest.raises(ValueError):
        included_file.add_host("existing_host")
