from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import DataFrame
    from types import ModuleType

class TableM:
    def __init__(
            self,
            data: DataFrame,
            experience: str,
            index = None,
            ex: float | int | None = None
    ):
        self.values = data
        self.values = self.values.set_index(index)
        self.experience_col = experience

        # If expected value not provided, set it equal to the mean of the sample data.
        if ex is None:
            self.ex = self.values[self.experience_col].mean()
        else:
            self.ex = ex

        self.values['Entry Ratio'] = self.values[self.experience_col] / self.ex

    def phi(self, r: float | int) -> float :

        df_res = self.values.copy()
        df_res['Limited Entry Ratio'] = df_res['Entry Ratio'].clip(upper=r)
        df_res['Difference'] = df_res['Entry Ratio'] - df_res['Limited Entry Ratio']
        charge = df_res['Difference'].sum() / df_res.shape[0]
        return charge

    def lee_diagram(
            self,
            xlabel: str = "Percent",
            ylabel: str = "Entry Ratio",
            title: str = "Table M Lee Diagram"
    ) -> ModuleType:

        entry_ratios = self.values['Entry Ratio'].sort_values(ascending=True).to_numpy()
        n_bars = len(entry_ratios)
        bar_width = 100 / n_bars

        fig, ax = plt.subplots()
        ax.bar(
            [i * bar_width for i in range(n_bars)],
            entry_ratios,
            width=bar_width,
            align='edge',
            edgecolor='white',
            linewidth=1
        )

        ax.set_xlim(0, 100)
        # Set x-axis label to cumulative percentage rank of observation.
        ax.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        return plt

    def __repr__(self) -> str:
        return self.values.__repr__()