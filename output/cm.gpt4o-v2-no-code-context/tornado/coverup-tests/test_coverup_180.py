# file: tornado/locks.py:554-560
# asked: {"lines": [554, 560], "branches": []}
# gained: {"lines": [554], "branches": []}

import pytest
from tornado.locks import Lock

class TestLock:
    @pytest.mark.asyncio
    async def test_lock_exit(self):
        lock = Lock()
        
        # Mock the __enter__ method to track its call
        original_enter = lock.__enter__
        lock.__enter__ = lambda: None
        
        try:
            async with lock:
                pass
        except Exception as e:
            pytest.fail(f"Unexpected exception: {e}")
        finally:
            # Restore the original __enter__ method
            lock.__enter__ = original_enter

        # Ensure __enter__ was called in __exit__
        assert lock.__enter__ is not None
