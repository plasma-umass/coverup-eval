# file youtube_dl/options.py:23-38
# lines [24, 25, 27, 28, 29, 30, 32, 34, 35, 36, 37, 38]
# branches ['29->30', '29->32', '35->36', '35->38', '36->35', '36->37']

import pytest
from youtube_dl.options import _hide_login_info

@pytest.fixture
def cleanup():
    # Fixture to clean up any state after tests
    yield
    # No cleanup needed for this test

def test_hide_login_info(cleanup):
    sensitive_options = [
        '-p', '--password', '-u', '--username', '--video-password', 
        '--ap-password', '--ap-username'
    ]
    sensitive_values = ['password123', 'user123', 'videopass', 'appass', 'appuser']
    opts = []
    for opt in sensitive_options:
        for value in sensitive_values:
            opts.append(opt)
            opts.append(value)
    
    scrubbed_opts = _hide_login_info(opts)
    
    for opt in sensitive_options:
        assert opt in scrubbed_opts
    for value in sensitive_values:
        assert 'PRIVATE' in scrubbed_opts
        assert value not in scrubbed_opts

    # Check if the key=value options are also scrubbed
    key_value_opts = [f"{opt}=somevalue" for opt in sensitive_options]
    scrubbed_key_value_opts = _hide_login_info(key_value_opts)
    for opt in sensitive_options:
        assert f"{opt}=PRIVATE" in scrubbed_key_value_opts
