# file tqdm/rich.py:78-113
# lines [96]
# branches ['95->96', '100->111']

import pytest
from tqdm.rich import tqdm_rich
from tqdm.std import TqdmExperimentalWarning
from rich.progress import Progress
from pytest_mock import MockerFixture

# Test function to cover line 96 and branch 100->111
def test_tqdm_rich_disable_and_progress_none(mocker: MockerFixture):
    # Mock the warning to prevent it from being output during the test
    mocker.patch('tqdm.rich.warn')

    # Create an instance with disable=True to cover line 96
    instance_disabled = tqdm_rich(disable=True)
    assert instance_disabled.disable is True

    # Mock the Progress class to prevent side effects and errors
    mocked_progress = mocker.patch('tqdm.rich.Progress', autospec=True)
    mocked_progress.return_value.__enter__.return_value = mocked_progress
    mocked_progress.return_value.add_task.return_value = 1  # Mock task ID

    # Create an instance with progress=None to cover branch 100->111
    instance_progress_none = tqdm_rich(progress=None, total=100)  # Set total to avoid TypeError
    assert mocked_progress.called
    assert instance_progress_none._task_id == 1

    # Clean up by exiting the progress bar context manager
    instance_progress_none._prog.__exit__(None, None, None)
