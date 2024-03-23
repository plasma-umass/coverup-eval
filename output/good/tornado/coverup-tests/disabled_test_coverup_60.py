# file tornado/queues.py:153-166
# lines [153, 154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166]
# branches ['154->155', '154->157', '157->158', '157->160']

import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.mark.gen_test
def test_queue_init_exceptions():
    with pytest.raises(TypeError):
        Queue(maxsize=None)

    with pytest.raises(ValueError):
        Queue(maxsize=-1)

@pytest.mark.gen_test
def test_queue_init():
    q = Queue(maxsize=5)
    assert q._maxsize == 5
    assert len(q._getters) == 0
    assert len(q._putters) == 0
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()

@pytest.fixture
def io_loop():
    loop = IOLoop.current()
    yield loop
    loop.clear_current()
    loop.close(all_fds=True)

@pytest.mark.gen_test
def test_queue_put_get(io_loop):
    q = Queue(maxsize=1)

    @gen.coroutine
    def put_item():
        yield q.put(1)
        yield q.put(2)  # This will block until 'get_item' retrieves an item

    @gen.coroutine
    def get_item():
        item = yield q.get()
        assert item == 1
        q.task_done()

    io_loop.spawn_callback(put_item)
    io_loop.run_sync(get_item)
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()

    @gen.coroutine
    def finish_task():
        q.task_done()
        yield q.join()  # This will block until all tasks are done

    io_loop.run_sync(finish_task)
    assert q._finished.is_set()
