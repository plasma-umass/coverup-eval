# file youtube_dl/downloader/f4m.py:285-300
# lines [286, 287, 288, 289, 290, 291, 292, 294, 295, 297, 298, 300]
# branches ['288->289', '288->297', '292->288', '292->294', '297->298', '297->300']

import pytest
from youtube_dl.downloader.f4m import F4mFD

@pytest.fixture
def mock_time_sleep(mocker):
    return mocker.patch('youtube_dl.downloader.f4m.time.sleep', return_value=None)

@pytest.fixture
def mock_report_error(mocker):
    return mocker.patch.object(F4mFD, 'report_error')

@pytest.fixture
def mock_get_bootstrap_from_url(mocker):
    def side_effect(url):
        return {'url': url}
    return mocker.patch.object(F4mFD, '_get_bootstrap_from_url', side_effect=side_effect)

@pytest.fixture
def mock_build_fragments_list(mocker):
    return mocker.patch('youtube_dl.downloader.f4m.build_fragments_list', return_value=[])

def test_update_live_fragments_no_fragments(mock_time_sleep, mock_report_error, mock_get_bootstrap_from_url, mock_build_fragments_list):
    f4m_fd = F4mFD(None, None)
    bootstrap_url = 'http://example.com/bootstrap'
    latest_fragment = 10

    fragments_list = f4m_fd._update_live_fragments(bootstrap_url, latest_fragment)

    assert fragments_list == []
    assert mock_report_error.called
    assert mock_report_error.call_args[0][0] == 'Failed to update fragments'
    assert mock_time_sleep.call_count == 30
    mock_get_bootstrap_from_url.assert_called_with(bootstrap_url)
    mock_build_fragments_list.assert_called()
