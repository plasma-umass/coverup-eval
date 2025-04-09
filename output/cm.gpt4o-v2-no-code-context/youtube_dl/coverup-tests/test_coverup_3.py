# file: youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [69, 70], "branches": []}
# gained: {"lines": [69, 70], "branches": []}

import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

class MockLinuxAcademyIE(LinuxAcademyIE):
    def _login(self):
        self.logged_in = True

@pytest.fixture
def linux_academy_ie():
    return MockLinuxAcademyIE()

def test_real_initialize_calls_login(linux_academy_ie, mocker):
    mock_login = mocker.patch.object(linux_academy_ie, '_login', wraps=linux_academy_ie._login)
    linux_academy_ie._real_initialize()
    mock_login.assert_called_once()
    assert linux_academy_ie.logged_in
