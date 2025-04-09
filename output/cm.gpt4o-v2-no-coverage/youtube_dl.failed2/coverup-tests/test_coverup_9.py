# file: youtube_dl/downloader/f4m.py:188-207
# asked: {"lines": [190, 191, 192, 193, 194, 195, 199, 200, 201, 202, 204, 205, 207], "branches": [[195, 199], [195, 204], [199, 200], [199, 201], [201, 195], [201, 202], [204, 205], [204, 207]]}
# gained: {"lines": [190, 191, 192, 193, 194, 195, 199, 200, 201, 202, 204, 205, 207], "branches": [[195, 199], [195, 204], [199, 200], [199, 201], [201, 195], [201, 202], [204, 205], [204, 207]]}

import pytest
from youtube_dl.downloader.f4m import build_fragments_list

def test_build_fragments_list_normal_case():
    boot_info = {
        'segments': [{'segment_run': [(1, 3), (2, 2)]}],
        'fragments': [{'fragments': [{'first': 1}]}],
        'live': False
    }
    result = build_fragments_list(boot_info)
    assert result == [(1, 1), (1, 2), (1, 3), (2, 4), (2, 5)]

def test_build_fragments_list_live_case():
    boot_info = {
        'segments': [{'segment_run': [(1, 4294967295)]}],
        'fragments': [{'fragments': [{'first': 1}]}],
        'live': True
    }
    result = build_fragments_list(boot_info)
    assert result == [(1, 1), (1, 2)]

def test_build_fragments_list_edge_case():
    boot_info = {
        'segments': [{'segment_run': [(1, 0)]}],
        'fragments': [{'fragments': [{'first': 1}]}],
        'live': False
    }
    result = build_fragments_list(boot_info)
    assert result == []

def test_build_fragments_list_live_trim_case():
    boot_info = {
        'segments': [{'segment_run': [(1, 3), (2, 2)]}],
        'fragments': [{'fragments': [{'first': 1}]}],
        'live': True
    }
    result = build_fragments_list(boot_info)
    assert result == [(2, 4), (2, 5)]
