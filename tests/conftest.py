from __future__ import annotations

import pytest

from hardhat.utils.utility_functions import load_sample
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame

@pytest.fixture
def brosius() -> DataFrame:
    df = load_sample('brosius')
    return df

@pytest.fixture
def atol():
    return 1e-4