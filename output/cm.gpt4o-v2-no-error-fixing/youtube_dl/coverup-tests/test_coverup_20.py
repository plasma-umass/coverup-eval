# file: youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

import pytest
from youtube_dl.postprocessor.common import PostProcessor

def test_postprocessor_run():
    pp = PostProcessor()
    info = {'filepath': 'dummy_path'}
    to_delete, updated_info = pp.run(info)
    
    assert to_delete == []
    assert updated_info == info
