# file tornado/locks.py:286-335
# lines [286, 287]
# branches []

import pytest
from tornado.ioloop import IOLoop
from tornado.locks import Semaphore
from tornado import gen
from collections import deque
from tornado.concurrent import Future

@pytest.fixture
def setup_simulator():
    futures_q = deque([Future() for _ in range(3)])

    async def simulator(futures):
        for f in futures:
            await gen.sleep(0)
            await gen.sleep(0)
            f.set_result(None)

    IOLoop.current().add_callback(simulator, list(futures_q))

    def use_some_resource():
        return futures_q.popleft()

    return use_some_resource

@pytest.mark.asyncio
async def test_semaphore(setup_simulator):
    use_some_resource = setup_simulator
    sem = Semaphore(2)

    async def worker(worker_id):
        await sem.acquire()
        try:
            print("Worker %d is working" % worker_id)
            await use_some_resource()
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()

    await gen.multi([worker(1), worker(2), worker(3)])

    assert sem._value == 2  # Ensure semaphore is released back to initial value
