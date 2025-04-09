# file: youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [69, 70], "branches": []}
# gained: {"lines": [69, 70], "branches": []}

import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

class TestLinuxAcademyIE:
    @pytest.fixture
    def ie(self, mocker):
        ie = LinuxAcademyIE()
        mocker.patch.object(ie, '_login', return_value=None)
        return ie

    def test_real_initialize(self, ie):
        ie._real_initialize()
        ie._login.assert_called_once()
