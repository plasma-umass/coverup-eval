# file tornado/httpclient.py:757-786
# lines [758, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 777, 778, 779, 781, 782, 783, 784, 785, 786]
# branches ['768->769', '768->786', '778->779', '778->781', '782->783', '782->784', '784->768', '784->785']

import pytest
from tornado.httpclient import HTTPClient, HTTPError
from tornado.options import options

@pytest.fixture
def mock_http_client(mocker):
    client = mocker.patch('tornado.httpclient.HTTPClient')
    client().fetch.side_effect = lambda *args, **kwargs: type('Response', (), {'headers': 'mock_headers', 'body': b'mock_body'})
    return client

def test_main_execution(mock_http_client, mocker):
    mocker.patch('tornado.options.define')
    parse_command_line = mocker.patch('tornado.options.parse_command_line', return_value=['http://example.com'])
    mocker.patch('tornado.options.options', print_headers=True, print_body=True, follow_redirects=True, validate_cert=True, proxy_host=None, proxy_port=None)
    print_mock = mocker.patch('builtins.print')

    from tornado.httpclient import main
    main()

    parse_command_line.assert_called_once()
    mock_http_client().fetch.assert_called_once_with(
        'http://example.com',
        follow_redirects=True,
        validate_cert=True,
        proxy_host=None,
        proxy_port=None,
    )
    assert print_mock.call_count == 2
    print_mock.assert_any_call('mock_headers')
    print_mock.assert_any_call('mock_body')
    mock_http_client().close.assert_called_once()
