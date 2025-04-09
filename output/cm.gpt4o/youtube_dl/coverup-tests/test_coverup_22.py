# file youtube_dl/downloader/fragment.py:17-19
# lines [19]
# branches []

import pytest
from youtube_dl.downloader.fragment import HttpQuietDownloader
from youtube_dl import YoutubeDL

def test_HttpQuietDownloader_to_screen(mocker):
    ydl = YoutubeDL()
    downloader = HttpQuietDownloader(ydl, {})
    mock_to_screen = mocker.patch.object(downloader, 'to_screen', wraps=downloader.to_screen)
    
    downloader.to_screen("test message")
    
    mock_to_screen.assert_called_once_with("test message")
