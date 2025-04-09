# file: flutils/packages.py:169-292
# asked: {"lines": [233, 247, 259, 260, 261, 262, 281], "branches": [[232, 233], [246, 247], [258, 259], [280, 281]]}
# gained: {"lines": [281], "branches": [[280, 281]]}

import pytest
from flutils.packages import bump_version

def test_bump_version_minor_with_pre_txt():
    assert bump_version('1.2a0', pre_release='a') == '1.2.1a0'

def test_bump_version_minor_with_alpha_to_beta():
    assert bump_version('1.2a0', pre_release='b') == '1.2.1b0'

def test_bump_version_patch_with_pre_txt():
    assert bump_version('1.2.3a0', position=2, pre_release='a') == '1.2.3a1'

def test_bump_version_patch_with_alpha_to_beta():
    assert bump_version('1.2.3a0', position=2, pre_release='b') == '1.2.3b0'

def test_bump_version_patch_with_pre_txt_b():
    assert bump_version('1.2.3b0', position=2, pre_release='b') == '1.2.3b1'

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Add any necessary cleanup code here
    yield
    # Reset any state if needed
