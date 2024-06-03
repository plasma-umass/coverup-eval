# file youtube_dl/extractor/linuxacademy.py:69-70
# lines [69, 70]
# branches []

import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

@pytest.fixture
def mock_login(mocker):
    return mocker.patch.object(LinuxAcademyIE, '_login')

def test_real_initialize(mock_login):
    ie = LinuxAcademyIE()
    ie._real_initialize()
    mock_login.assert_called_once()
