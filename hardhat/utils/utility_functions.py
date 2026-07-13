from __future__ import annotations

import os
from typing import TYPE_CHECKING, AnyStr

import pandas as pd

if TYPE_CHECKING:
    from pandas import DataFrame


def load_sample(key: str) -> DataFrame:

    utils_path: AnyStr = os.path.dirname(os.path.abspath(__file__))

    return pd.read_csv(utils_path + '/data/' + key + '.csv')
