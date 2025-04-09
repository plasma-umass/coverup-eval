# file youtube_dl/downloader/f4m.py:188-207
# lines [190, 191, 192, 193, 194, 195, 199, 200, 201, 202, 204, 205, 207]
# branches ['195->199', '195->204', '199->200', '199->201', '201->195', '201->202', '204->205', '204->207']

import itertools
import pytest

# Assuming the existence of the build_fragments_list function within the module youtube_dl.downloader.f4m
from youtube_dl.downloader.f4m import build_fragments_list

def test_build_fragments_list_with_live_stream(mocker):
    # Mocking the boot_info to simulate a live stream with abnormal fragments_count
    boot_info = {
        'live': True,
        'segments': [{'segment_run': [(1, 4294967295)]}],
        'fragments': [{'fragments': [{'first': 1}]}]
    }

    # Expected result should only contain the last two fragments due to the live stream condition
    expected_result = [(1, 1), (1, 2)]

    # Run the test
    result = build_fragments_list(boot_info)

    # Assertions to verify the postconditions
    assert result == expected_result, "The result should only contain the last two fragments for a live stream"

    # No cleanup is necessary as the test does not affect any external state or files
