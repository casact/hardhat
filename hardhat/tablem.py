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

    def phi(self, r: float | int) -> float | int :
        """
        Calculate the insurance charge for the given entry ratio r.

        Parameters
        ----------
         r: float | int
            The entry ratio.

        Returns
        -------
        float | int
            The insurance charge.
        """
        df_res = self.values.copy()
        df_res['Limited Entry Ratio'] = df_res['Entry Ratio'].clip(upper=r)
        df_res['Difference'] = df_res['Entry Ratio'] - df_res['Limited Entry Ratio']
        charge = df_res['Difference'].sum() / df_res.shape[0]
        return charge

    def lee_diagram(
            self,
            xlabel: str = "Percent",
            ylabel: str = "Entry Ratio",
            title: str = "Table M Lee Diagram",
            r: float | int | None = None,
            rcolor: str | None = None,
            orientation: str = "vertical"
    ) -> ModuleType:
        """
        Draw a Lee diagram.

        Parameters
        ----------
        xlabel: str, default "Percent"
            The x-axis label.
        ylabel: str, default "Entry Ratio"
            The y-axis label.
        title: str, default "Table M Lee Diagram"
            The chart title.
        r: float | int | None, optional
            The entry ratio. If supplied, the chart will draw a horizontal line at its value.
        rcolor: str | None, optional,
            The color of the entry ratio line, defaults to red if drawn.
        orientation: str, default "vertical"
            The orientation of the bars in the Lee diagram.

        Returns
        -------
        ModuleType
            A matplotlib.pyplot module.

        """

        entry_ratios = self.values['Entry Ratio'].sort_values(ascending=True).to_numpy()
        n_bars = len(entry_ratios)
        bar_width = 100 / n_bars

        fig, ax = plt.subplots()

        if orientation == "horizontal":
            heights = [entry_ratios[i] - (entry_ratios[i - 1] if i > 0 else 0) for i in range(n_bars)]
            bottoms = [entry_ratios[i - 1] if i > 0 else 0 for i in range(n_bars)]
            widths = [(n_bars - i) * bar_width for i in range(n_bars)]
            lefts = [100 - width for width in widths]

            ax.barh(
                bottoms,
                widths,
                height=heights,
                left=lefts,
                align='edge',
                edgecolor='white',
                linewidth=1
            )
            ax.set_ylim(bottom=0)
        else:
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

        if r is not None:
            ax.axhline(y=r, color=rcolor or 'red')

        return plt

    def __repr__(self) -> str:
        return self.values.__repr__()