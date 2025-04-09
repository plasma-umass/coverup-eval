# file tornado/locks.py:398-413
# lines [398, 400, 401, 402, 403, 404, 412, 413]
# branches ['401->exit', '401->402', '403->401', '403->404']

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.fixture
def semaphore():
    return Semaphore(0)

@pytest.mark.gen_test
async def test_semaphore_release_with_waiter(semaphore):
    waiter = gen.Future()
    semaphore._waiters.append(waiter)
    semaphore.release()
    await waiter  # This line is necessary to allow the Future to run and be set.
    assert semaphore._value == 0
    assert waiter.done()
    assert isinstance(waiter.result(), Semaphore._ReleasingContextManager)

@pytest.mark.gen_test
async def test_semaphore_release_without_waiter(semaphore):
    semaphore.release()
    assert semaphore._value == 1

@pytest.mark.gen_test
async def test_semaphore_release_with_done_waiter(semaphore):
    waiter = gen.Future()
    waiter.set_result(None)
    semaphore._waiters.append(waiter)
    semaphore.release()
    assert semaphore._value == 1
    assert waiter.done()

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code to ensure isolation between tests
    yield
    IOLoop.clear_current()
