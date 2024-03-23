# file sanic/models/futures.py:43-53
# lines [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
# branches []

import pytest
from sanic.models.futures import FutureStatic
from pathlib import PurePath

@pytest.fixture
def future_static_instance():
    return FutureStatic(
        uri='/test_uri',
        file_or_directory=PurePath('/test/path'),
        pattern='*.txt',
        use_modified_since=True,
        use_content_range=True,
        stream_large_files=False,
        name='test_name',
        host='localhost',
        strict_slashes=True,
        content_type='text/plain'
    )

def test_future_static(future_static_instance):
    assert future_static_instance.uri == '/test_uri'
    assert isinstance(future_static_instance.file_or_directory, PurePath)
    assert future_static_instance.pattern == '*.txt'
    assert future_static_instance.use_modified_since is True
    assert future_static_instance.use_content_range is True
    assert future_static_instance.stream_large_files is False
    assert future_static_instance.name == 'test_name'
    assert future_static_instance.host == 'localhost'
    assert future_static_instance.strict_slashes is True
    assert future_static_instance.content_type == 'text/plain'
