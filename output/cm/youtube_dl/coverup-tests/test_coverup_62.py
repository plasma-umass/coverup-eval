# file youtube_dl/postprocessor/metadatafromtitle.py:8-48
# lines [10, 11, 12, 13, 14, 23, 24, 26, 27, 28, 29, 30, 31, 32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48]
# branches ['26->27', '26->30', '30->31', '30->32', '37->38', '37->42', '42->43', '42->48']

import pytest
from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP

def test_metadata_from_title_pp(mocker):
    # Mock the downloader and its to_screen method to avoid side effects
    downloader_mock = mocker.Mock()
    downloader_mock.to_screen = mocker.Mock()

    # Test case to cover lines 10-14, 23-32, 35-48
    titleformat = '%(artist)s - %(title)s'
    info = {'title': 'Coldplay - Yellow'}

    # Create an instance of MetadataFromTitlePP
    pp = MetadataFromTitlePP(downloader_mock, titleformat)

    # Run the postprocessor
    _, new_info = pp.run(info)

    # Assertions to check if the regex conversion and matching worked
    assert pp._titleregex == r'(?P<artist>.+)\ \-\ (?P<title>.+)', "The title format regex conversion failed"
    assert new_info['artist'] == 'Coldplay', "The artist was not correctly extracted from the title"
    assert new_info['title'] == 'Yellow', "The title was not correctly extracted from the title"

    # Assertions to check if the to_screen method was called with the correct arguments
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed artist: Coldplay')
    downloader_mock.to_screen.assert_any_call('[fromtitle] parsed title: Yellow')

    # Test case to cover line 37-41 (no match)
    info_no_match = {'title': 'This will not match'}
    _, new_info_no_match = pp.run(info_no_match)

    # Assertions to check if the to_screen method was called with the correct arguments when no match is found
    downloader_mock.to_screen.assert_called_with('[fromtitle] Could not interpret title of video as "%(artist)s - %(title)s"')
    assert new_info_no_match == info_no_match, "The info should not be modified if the title does not match the format"
