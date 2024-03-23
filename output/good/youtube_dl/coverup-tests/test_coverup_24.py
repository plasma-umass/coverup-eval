# file youtube_dl/downloader/common.py:368-370
# lines [368, 370]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    def test_real_download_not_implemented(self, mocker, tmp_path):
        # Mock the __init__ method of FileDownloader to not require any parameters
        mocker.patch.object(FileDownloader, '__init__', return_value=None)

        # Create a subclass of FileDownloader that does not override real_download
        class TestDownloader(FileDownloader):
            pass

        # Instantiate the subclass
        downloader = TestDownloader()

        # Define a dummy filename and info_dict
        dummy_filename = tmp_path / "dummy_video.txt"
        dummy_info_dict = {}

        # Expect NotImplementedError when calling real_download
        with pytest.raises(NotImplementedError):
            downloader.real_download(str(dummy_filename), dummy_info_dict)
