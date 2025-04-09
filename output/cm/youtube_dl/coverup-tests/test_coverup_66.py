# file youtube_dl/extractor/safari.py:31-82
# lines [32, 33, 34, 36, 37, 38, 40, 41, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 72, 73, 75, 76, 78, 79, 80, 82]
# branches ['33->34', '33->36', '43->44', '43->47', '65->67', '65->72', '72->73', '72->75', '78->79', '78->82']

import json
import pytest
from youtube_dl.extractor.safari import SafariBaseIE
from youtube_dl.utils import ExtractorError

@pytest.fixture
def safari_extractor(mocker):
    extractor = SafariBaseIE()
    extractor._get_login_info = mocker.Mock(return_value=('user', 'pass'))
    extractor._download_webpage_handle = mocker.Mock()
    extractor._download_json_handle = mocker.Mock()
    extractor._apply_first_set_cookie_header = mocker.Mock()
    return extractor

def test_login_success(safari_extractor, mocker):
    # Mocking the responses for successful login
    mocker.patch('youtube_dl.extractor.safari.compat_urlparse.urlparse', return_value=mocker.Mock(query='next=%2Fhome%2F'))
    mocker.patch('youtube_dl.extractor.safari.compat_parse_qs', return_value={'next': ['/home/']})
    mocker.patch('youtube_dl.extractor.safari.compat_urlparse.urljoin', return_value='https://api.oreilly.com/home/')
    
    # Mocking the webpage handle to simulate the login check
    safari_extractor._download_webpage_handle.return_value = (None, mocker.Mock(geturl=lambda: 'https://learning.oreilly.com/home/'))
    
    # Mocking the json handle to simulate the login response
    safari_extractor._download_json_handle.return_value = ({'logged_in': True, 'redirect_uri': 'https://learning.oreilly.com/home/'}, mocker.Mock())
    
    safari_extractor._login()
    
    # Assertions to check if the login was successful
    assert safari_extractor.LOGGED_IN is True
    safari_extractor._apply_first_set_cookie_header.assert_not_called()

def test_login_failure(safari_extractor, mocker):
    # Mocking the responses for failed login
    mocker.patch('youtube_dl.extractor.safari.compat_urlparse.urlparse', return_value=mocker.Mock(query='next=%2Fhome%2F'))
    mocker.patch('youtube_dl.extractor.safari.compat_parse_qs', return_value={'next': ['/home/']})
    mocker.patch('youtube_dl.extractor.safari.compat_urlparse.urljoin', return_value='https://api.oreilly.com/home/')
    
    # Mocking the webpage handle to simulate the login check
    safari_extractor._download_webpage_handle.return_value = (None, mocker.Mock(geturl=lambda: 'https://learning.oreilly.com/accounts/login-check/'))
    
    # Mocking the json handle to simulate the login response
    safari_extractor._download_json_handle.return_value = ({'logged_in': False, 'credentials': 'Invalid credentials'}, mocker.Mock())
    
    with pytest.raises(ExtractorError) as exc_info:
        safari_extractor._login()
    
    # Assertions to check if the login failed with the correct error message
    assert 'Unable to login: Invalid credentials' in str(exc_info.value)
