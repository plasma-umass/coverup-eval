# file youtube_dl/postprocessor/xattrpp.py:26-79
# lines [51, 52, 54, 55, 56, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 77, 78, 79]
# branches ['50->51', '51->52', '51->54', '65->66', '65->69', '69->70', '69->73', '74->75', '74->77']

import pytest
from youtube_dl.postprocessor.xattrpp import XAttrMetadataPP
from youtube_dl.utils import XAttrUnavailableError, XAttrMetadataError

class MockDownloader:
    def to_screen(self, message):
        pass

    def report_error(self, message):
        pass

    def report_warning(self, message):
        pass

def test_xattr_metadata_pp(mocker):
    # Mock the necessary parts
    mock_write_xattr = mocker.patch('youtube_dl.postprocessor.xattrpp.write_xattr')
    mocker.patch('youtube_dl.postprocessor.xattrpp.hyphenate_date', return_value='2023-01-01')
    mock_downloader = MockDownloader()

    # Create an instance of the postprocessor
    pp = XAttrMetadataPP(mock_downloader)

    # Test data
    info = {
        'filepath': 'testfile',
        'webpage_url': 'https://example.com',
        'title': 'Test Title',
        'upload_date': '20230101',
        'description': 'Test Description',
        'uploader': 'Test Uploader',
        'format': 'mp4'
    }

    # Run the postprocessor
    pp.run(info)

    # Assert that write_xattr was called
    assert mock_write_xattr.call_count == 6

    # Test XAttrUnavailableError
    mock_write_xattr.side_effect = XAttrUnavailableError('Unavailable')
    pp.run(info)
    mock_write_xattr.side_effect = None

    # Test XAttrMetadataError with different reasons
    for reason in ['NO_SPACE', 'VALUE_TOO_LONG', 'OTHER']:
        mock_write_xattr.side_effect = XAttrMetadataError(reason)
        pp.run(info)
        mock_write_xattr.side_effect = None

    # Cleanup
    mocker.stopall()
