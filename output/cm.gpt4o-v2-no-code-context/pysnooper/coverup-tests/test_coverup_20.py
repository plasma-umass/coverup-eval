# file: pysnooper/tracer.py:339-498
# asked: {"lines": [347, 348, 352, 353, 354, 356, 357, 358, 359, 360, 361, 362, 364, 366, 367, 368, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 386, 387, 388, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 406, 407, 408, 409, 413, 414, 415, 416, 417, 418, 421, 422, 424, 425, 426, 427, 428, 429, 430, 438, 441, 442, 443, 444, 447, 449, 451, 452, 453, 460, 461, 462, 463, 464, 465, 466, 467, 470, 471, 472, 474, 475, 477, 478, 479, 480, 482, 483, 484, 485, 486, 488, 489, 491, 492, 493, 494, 495, 496, 498], "branches": [[347, 348], [347, 366], [348, 352], [348, 353], [353, 354], [353, 356], [357, 358], [357, 364], [359, 360], [359, 361], [361, 357], [361, 362], [366, 367], [366, 368], [375, 376], [375, 377], [377, 378], [377, 386], [396, 397], [396, 400], [402, 403], [402, 409], [403, 404], [403, 406], [424, 425], [424, 438], [425, 426], [425, 428], [428, 424], [428, 429], [438, 441], [438, 460], [441, 442], [441, 460], [449, 441], [449, 451], [461, 462], [461, 463], [470, 471], [470, 474], [477, 478], [477, 491], [482, 483], [482, 491], [491, 492], [491, 498], [493, 494], [493, 495]]}
# gained: {"lines": [347, 348, 352, 353, 354, 356, 357, 358, 359, 361, 364, 366, 367, 368, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 386, 387, 388, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 406, 407, 408, 409, 413, 414, 415, 416, 417, 418, 421, 422, 424, 438, 441, 442, 443, 449, 451, 452, 453, 460, 461, 463, 464, 465, 466, 467, 470, 471, 472, 474, 475, 477, 478, 479, 480, 482, 491, 492, 493, 495, 496, 498], "branches": [[347, 348], [347, 366], [348, 352], [348, 353], [353, 354], [353, 356], [357, 358], [357, 364], [359, 361], [361, 357], [366, 367], [366, 368], [375, 376], [375, 377], [377, 378], [377, 386], [396, 397], [402, 403], [402, 409], [403, 406], [424, 438], [438, 441], [438, 460], [441, 442], [449, 451], [461, 463], [470, 471], [470, 474], [477, 478], [477, 491], [482, 491], [491, 492], [491, 498], [493, 495]]}

import pytest
import threading
import datetime as datetime_module
import itertools
import os
import opcode
import traceback
from unittest.mock import MagicMock, patch

from pysnooper.tracer import Tracer, get_path_and_source_from_frame, pycompat, utils

@pytest.fixture
def tracer():
    tracer = Tracer()
    tracer.target_codes = set()
    tracer.target_frames = set()
    tracer.depth = 1
    tracer.normalize = False
    tracer.relative_time = False
    tracer.start_times = {}
    tracer.last_source_path = None
    tracer.thread_info = False
    tracer.watch = []
    tracer.custom_repr = None
    tracer.max_variable_length = None
    return tracer

@pytest.fixture
def frame():
    frame = MagicMock()
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None
    return frame

@pytest.fixture
def thread_global():
    class ThreadGlobal:
        depth = 0
    return ThreadGlobal()

def test_trace_should_not_trace(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set()
    tracer.target_frames = set()
    tracer.depth = 1

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    assert tracer.trace(frame, 'call', None) is None

def test_trace_internal_frame(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set()
    tracer.target_frames = set()
    tracer.depth = 2

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)
    monkeypatch.setattr(tracer, '_is_internal_frame', lambda x: True)

    assert tracer.trace(frame, 'call', None) is None

def test_trace_depth(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = MagicMock()
    frame.f_back.f_code = MagicMock()
    frame.f_back.f_code.co_code = b'\x00'
    frame.f_back.f_lasti = 0
    frame.f_back.f_lineno = 1
    frame.f_back.f_back = None

    tracer.target_codes = set()
    tracer.target_frames = set()
    tracer.depth = 2

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)
    monkeypatch.setattr(tracer, '_is_internal_frame', lambda x: False)

    assert tracer.trace(frame, 'call', None) is None

def test_trace_event_call(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set([frame.f_code])
    tracer.target_frames = set()
    tracer.depth = 1

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    tracer.trace(frame, 'call', None)
    assert thread_global.depth == 1

def test_trace_event_return(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set([frame.f_code])
    tracer.target_frames = set()
    tracer.depth = 1

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    tracer.trace(frame, 'return', None)
    assert thread_global.depth == -1

def test_trace_event_exception(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set([frame.f_code])
    tracer.target_frames = set()
    tracer.depth = 1

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    tracer.trace(frame, 'exception', (Exception, Exception("test"), None))
    assert thread_global.depth == 0

def test_trace_normalize(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set([frame.f_code])
    tracer.target_frames = set()
    tracer.depth = 1
    tracer.normalize = True

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    tracer.trace(frame, 'call', None)
    assert thread_global.depth == 1

def test_trace_relative_time(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set([frame.f_code])
    tracer.target_frames = set()
    tracer.depth = 1
    tracer.relative_time = True

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    tracer.trace(frame, 'call', None)
    assert thread_global.depth == 1

def test_trace_thread_info(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set([frame.f_code])
    tracer.target_frames = set()
    tracer.depth = 1
    tracer.thread_info = True

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    tracer.trace(frame, 'call', None)
    assert thread_global.depth == 1

def test_trace_exception_handling(tracer, frame, thread_global, monkeypatch):
    frame.f_code = MagicMock()
    frame.f_code.co_code = b'\x00'
    frame.f_lasti = 0
    frame.f_lineno = 1
    frame.f_back = None

    tracer.target_codes = set([frame.f_code])
    tracer.target_frames = set()
    tracer.depth = 1

    monkeypatch.setattr('pysnooper.tracer.thread_global', thread_global)

    tracer.trace(frame, 'exception', (Exception, Exception("test"), None))
    assert thread_global.depth == 0
