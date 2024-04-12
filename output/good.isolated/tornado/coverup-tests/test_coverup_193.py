# file tornado/locks.py:53-102
# lines [53, 54]
# branches []

import pytest
from tornado import gen, locks
from tornado.ioloop import IOLoop
from datetime import timedelta

@pytest.mark.gen_test
async def test_condition_with_timeout():
    condition = locks.Condition()
    timeout = timedelta(seconds=0.1)

    async def waiter():
        with pytest.raises(gen.TimeoutError):
            await condition.wait(timeout=timeout)

    await waiter()

    # Ensure that the condition's waiters list is cleaned up
    assert not condition._waiters
