# file youtube_dl/extractor/linuxacademy.py:69-70
# lines [69, 70]
# branches []

import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE
from youtube_dl.utils import ExtractorError

@pytest.fixture
def mock_login(mocker):
    mocker.patch.object(LinuxAcademyIE, '_login')

def test_linux_academy_real_initialize(mock_login):
    # Create an instance of the LinuxAcademyIE class
    ie = LinuxAcademyIE()
    
    # Call the _real_initialize method which should call the _login method
    ie._real_initialize()
    
    # Assert that the _login method was called
    assert LinuxAcademyIE._login.called, "The _login method should be called during initialization"
