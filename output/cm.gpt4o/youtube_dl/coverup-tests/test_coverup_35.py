# file youtube_dl/postprocessor/common.py:41-56
# lines [56]
# branches []

import pytest
from youtube_dl.postprocessor.common import PostProcessor

def test_postprocessor_run():
    pp = PostProcessor()
    information = {
        'filepath': '/path/to/downloaded/file',
        'title': 'Sample Video',
        'uploader': 'Sample Uploader'
    }
    
    # Run the PostProcessor
    files_to_delete, updated_information = pp.run(information)
    
    # Assertions to verify the postconditions
    assert files_to_delete == []
    assert updated_information == information

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
