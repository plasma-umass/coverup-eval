# file tornado/locks.py:443-444
# lines [443, 444]
# branches []

import pytest
from tornado.locks import Semaphore

@pytest.mark.asyncio
async def test_semaphore_with_statement():
    semaphore = Semaphore()

    with pytest.raises(RuntimeError) as exc_info:
        with semaphore:
            pass  # This block should never be executed

    assert "Use 'async with' instead of 'with' for Semaphore" in str(exc_info.value)
