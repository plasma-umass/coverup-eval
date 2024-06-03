# file youtube_dl/extractor/safari.py:242-245
# lines [244, 245]
# branches []

import pytest
from youtube_dl.extractor.safari import SafariCourseIE, SafariIE, SafariApiIE

@pytest.fixture
def mock_safari_ie(mocker):
    mocker.patch.object(SafariIE, 'suitable', return_value=False)
    mocker.patch.object(SafariApiIE, 'suitable', return_value=False)
    yield
    mocker.stopall()

def test_safari_course_ie_suitable_false(mock_safari_ie, mocker):
    mock_super_suitable = mocker.patch('youtube_dl.extractor.safari.SafariBaseIE.suitable', return_value=True)
    url = 'http://example.com/course'
    assert SafariCourseIE.suitable(url) is True
    mock_super_suitable.assert_called_once_with(url)

def test_safari_course_ie_suitable_true(mocker):
    mocker.patch.object(SafariIE, 'suitable', return_value=True)
    url = 'http://example.com/course'
    assert SafariCourseIE.suitable(url) is False

def test_safari_course_ie_suitable_api_true(mocker):
    mocker.patch.object(SafariApiIE, 'suitable', return_value=True)
    url = 'http://example.com/course'
    assert SafariCourseIE.suitable(url) is False
