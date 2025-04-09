# file tornado/locks.py:446-452
# lines [446, 452]
# branches []

import pytest
from tornado.locks import Semaphore
from unittest.mock import Mock
import asyncio

@pytest.fixture
def semaphore():
    return Semaphore(value=1)

@pytest.mark.asyncio
async def test_semaphore_context_manager(semaphore):
    async with semaphore as sem:
        assert semaphore._value == 0  # The semaphore should be acquired

    # After the async with block, the semaphore should be released
    assert semaphore._value == 1

@pytest.mark.asyncio
async def test_semaphore_context_manager_exception(semaphore):
    with pytest.raises(RuntimeError):
        async with semaphore as sem:
            assert semaphore._value == 0  # The semaphore should be acquired
            raise RuntimeError("An exception occurred")

    # After the async with block with an exception, the semaphore should be released
    assert semaphore._value == 1

@pytest.mark.asyncio
async def test_semaphore_context_manager_with_mock(mocker):
    mock_enter = mocker.patch.object(Semaphore, '__enter__', return_value=None)
    mock_exit = mocker.patch.object(Semaphore, '__exit__', return_value=None)

    async with semaphore:
        pass

    mock_enter.assert_not_called()  # __enter__ is not called because it's an async context manager
    mock_exit.assert_not_called()   # __exit__ is not called because it's an async context manager
