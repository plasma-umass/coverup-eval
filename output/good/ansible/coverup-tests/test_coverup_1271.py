# file lib/ansible/executor/powershell/module_manifest.py:254-261
# lines [255, 256, 257, 258, 259, 260, 261]
# branches ['255->256', '255->258']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import _slurp

def test_slurp_nonexistent_file(mocker):
    path = "/nonexistent/path/to/file"
    mocker.patch.object(os.path, 'exists', return_value=False)
    with pytest.raises(AnsibleError) as excinfo:
        _slurp(path)
    assert "imported module support code does not exist at" in str(excinfo.value)
