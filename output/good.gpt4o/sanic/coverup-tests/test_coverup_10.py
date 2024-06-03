# file sanic/exceptions.py:9-21
# lines [9, 14, 15, 16, 17, 18, 19, 21]
# branches ['16->17', '16->18']

import pytest
from sanic.exceptions import add_status_code

# Mock dictionary to simulate _sanic_exceptions
@pytest.fixture
def mock_sanic_exceptions(mocker):
    return mocker.patch('sanic.exceptions._sanic_exceptions', {})

def test_add_status_code(mock_sanic_exceptions):
    @add_status_code(404)
    class NotFoundException(Exception):
        pass

    @add_status_code(500, quiet=False)
    class InternalServerErrorException(Exception):
        pass

    @add_status_code(400, quiet=True)
    class BadRequestException(Exception):
        pass

    # Assertions to verify the status codes and quiet attributes
    assert NotFoundException.status_code == 404
    assert NotFoundException.quiet is True
    assert mock_sanic_exceptions[404] is NotFoundException

    assert InternalServerErrorException.status_code == 500
    assert not hasattr(InternalServerErrorException, 'quiet')
    assert mock_sanic_exceptions[500] is InternalServerErrorException

    assert BadRequestException.status_code == 400
    assert BadRequestException.quiet is True
    assert mock_sanic_exceptions[400] is BadRequestException
