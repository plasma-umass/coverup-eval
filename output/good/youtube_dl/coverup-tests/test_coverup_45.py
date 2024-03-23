# file youtube_dl/extractor/safari.py:247-264
# lines [248, 250, 251, 252, 254, 255, 256, 258, 259, 260, 262, 264]
# branches ['254->255', '254->258']

import pytest
from youtube_dl.extractor.safari import SafariCourseIE
from youtube_dl.utils import ExtractorError

def test_safari_course_extraction(mocker):
    # Mock the _match_id method to return a fake course_id
    course_id = 'fake_course_id'
    mocker.patch.object(SafariCourseIE, '_match_id', return_value=course_id)

    # Mock the _download_json method to return a fake course JSON
    fake_course_json = {
        'chapters': ['chapter1', 'chapter2'],
        'title': 'Fake Course Title'
    }
    mocker.patch.object(SafariCourseIE, '_download_json', return_value=fake_course_json)

    # Mock the url_result method to return a fake result
    mocker.patch('youtube_dl.extractor.safari.SafariApiIE.ie_key', return_value='SafariApi')
    mocker.patch('youtube_dl.extractor.safari.SafariCourseIE.url_result', side_effect=lambda x, y: {'url': x})

    # Create an instance of the extractor and call the _real_extract method
    extractor = SafariCourseIE()
    result = extractor._real_extract('http://fake.url/course')

    # Assertions to check if the result is as expected
    assert result['id'] == course_id
    assert result['title'] == fake_course_json['title']
    assert len(result['entries']) == len(fake_course_json['chapters'])
    for entry, chapter in zip(result['entries'], fake_course_json['chapters']):
        assert entry['url'] == chapter

    # Check if the ExtractorError is raised when 'chapters' key is missing
    mocker.patch.object(SafariCourseIE, '_download_json', return_value={'title': 'No Chapters'})
    with pytest.raises(ExtractorError) as exc_info:
        extractor._real_extract('http://fake.url/course')
    assert 'No chapters found for course' in str(exc_info.value)
