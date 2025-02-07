# file: youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [69, 70], "branches": []}
# gained: {"lines": [69, 70], "branches": []}

import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

@pytest.fixture
def linux_academy_ie(mocker):
    ie = LinuxAcademyIE()
    mocker.patch.object(ie, '_login')
    return ie

def test_real_initialize(linux_academy_ie):
    linux_academy_ie._real_initialize()
    linux_academy_ie._login.assert_called_once()
