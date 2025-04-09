# file tornado/locks.py:539-549
# lines [539, 546, 547, 548, 549]
# branches []

import pytest
from tornado.locks import Lock

def test_lock_release_unlocked(mocker):
    lock = Lock()
    mocker.patch.object(lock._block, 'release', side_effect=ValueError)
    
    with pytest.raises(RuntimeError, match="release unlocked lock"):
        lock.release()
