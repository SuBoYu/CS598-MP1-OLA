from typing import List
import numpy as np
import pandas as pd
import plotly.graph_objects as go

"""
****************************************
* You do not have to modify this file. *
****************************************
"""


def sample_split_df(df: pd.DataFrame, sample_percentage: float = 0.1, slice_size: int = 20000) -> List[pd.DataFrame]:
    """
        Sample from a dataframe, then split it into slices row-wise.

        @param df: dataframe to sample and split.
        @param sample_percentage: percentage of rows to sample.
        @param slice_size: size of each dataframe slice. Note that the last slice may have less than *slice_size* rows.
    """
    np.random.seed(42)
    # Create a sample of the dataframe without replacement
    df_sample = df.sample(frac=sample_percentage, replace=False, random_state=42)

    # Divide the sample into slices for incremental processing
    df_slice_list = []
    for i in range(0, df_sample.shape[0], slice_size):
        df_slice_list.append(df_sample[i:min(i + slice_size, df_sample.shape[0])])

    return df_slice_list


def generate_plot(title: str, xaxis_title: str, yaxis_title: str) -> go.FigureWidget:
    """
        Create a plotly plot with the specified text components.

        @param title: plot title.
        @param xaxis_title: x axis title.
        @param yaxis_title: y axis title.
    """
    a = ['wait for data']
    b = [0]

    fig = go.Figure(data=[go.Bar(x=a, y=b, width=0.3)])
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="Black"
        )
    )
    return go.FigureWidget(fig)
