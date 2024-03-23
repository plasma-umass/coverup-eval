# file youtube_dl/downloader/common.py:126-137
# lines [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]
# branches ['130->131', '130->132', '133->134', '133->135', '135->136', '135->137']

import pytest
from youtube_dl.downloader.common import FileDownloader

def test_best_block_size():
    # Test for elapsed_time < 0.001
    block_size = FileDownloader.best_block_size(0.0005, 1000)
    assert block_size == 2000, "Should return the doubled bytes as block size"

    # Test for rate > new_max
    block_size = FileDownloader.best_block_size(1, 10**7)
    assert block_size == 4194304, "Should return the maximum block size"

    # Test for rate < new_min
    block_size = FileDownloader.best_block_size(10, 1)
    assert block_size == 1, "Should return the minimum block size"

    # Test for new_min <= rate <= new_max
    block_size = FileDownloader.best_block_size(1, 2000)
    assert block_size == 2000, "Should return the rate as block size"

    # Test for bytes < 1 (should return 1 as the block size)
    block_size = FileDownloader.best_block_size(1, 0.5)
    assert block_size == 1, "Should return the minimum block size"

    # Test for bytes > 4194304 (should return 4194304 as the block size)
    block_size = FileDownloader.best_block_size(1, 10**8)
    assert block_size == 4194304, "Should return the maximum block size"

# Note: No cleanup is necessary for these tests as they do not modify any external state.
