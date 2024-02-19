from HLL import HyperLogLog
from typing import List, Any

import pandas as pd
import plotly.graph_objects as go


class OLA:
    def __init__(self, widget: go.FigureWidget):
        """
            Base OLA class.

            *****************************************
            * You do not have to modify this class. *
            *****************************************

            @param widget: The dynamically updating plotly plot.
        """
        self.widget = widget

    def process_slice(df_slice: pd.DataFrame) -> None:
        """
            Process a dataframe slice. To be implemented in inherited classes.
        """
        pass

    def update_widget(self, groups_list: List[Any], values_list: List[Any]) -> None:
        """
            Update the plotly widget with newest groupings and values.

            @param groups_list: List of groups.
            @param values_list: List of grouped values (e.g., grouped means/sums).
        """
        self.widget.data[0]['x'] = groups_list
        self.widget.data[0]['y'] = values_list


class AvgOla(OLA):
    def __init__(self, widget: go.FigureWidget, mean_col: str):
        """
            Class for performing OLA by incrementally computing the estimated mean of *mean_col*.
            This class is implemented for you as an example.

            @param mean_col: column to compute filtered mean for.
        """
        super().__init__(widget)
        self.mean_col = mean_col

        # Bookkeeping variables
        self.sum = 0
        self.count = 0

    def process_slice(self, df_slice: pd.DataFrame) -> None:
        """
            Update the running mean with a data frame slice.
        """
        self.sum += df_slice.sum()[self.mean_col]
        self.count += df_slice.count()[self.mean_col]

        # Update the plot. The mean should be put into a singleton list due to Plotly semantics.
        # Note: there is no x axis label since there is only one bar.
        self.update_widget([""], [self.sum / self.count])


class FilterAvgOla(OLA):
    def __init__(self, widget: go.FigureWidget, filter_col: str, filter_value: Any, mean_col: str):
        """
            Class for performing OLA by incrementally computing the estimated filtered mean of *mean_col*
            where *filter_col* is equal to *filter_value*.

            @param filter_col: column to filter on.
            @param filter_value: value to filter for, i.e., df[df[filter_col] == filter_value].
            @param mean_col: column to compute filtered mean for.
        """
        super().__init__(widget)
        self.filter_col = filter_col
        self.filter_value = filter_value
        self.mean_col = mean_col

        # Put any other bookkeeping class variables you need here...
        self.sum = 0
        self.count = 0

    def process_slice(self, df_slice: pd.DataFrame) -> None:
        """
            Update the running filtered mean with a dataframe slice.
        """
        # Implement me!
        df_slice = df_slice[df_slice[self.filter_col]==self.filter_value]
        self.sum += df_slice.sum()[self.mean_col]
        self.count += df_slice.count()[self.mean_col]

        # Update the plot. The filtered mean should be put into a singleton list due to Plotly semantics.
        # hint: self.update_widget([""], *estimated filtered mean of mean_col*)
        self.update_widget([""], [self.sum / self.count])


class GroupByAvgOla(OLA):
    def __init__(self, widget: go.FigureWidget, groupby_col: str, mean_col: str):
        """
            Class for performing OLA by incrementally computing the estimated grouped means of *mean_col*
            with *groupby_col* as groups.

            @param groupby_col: grouping column, i.e., df.groupby(groupby_col).
            @param mean_col: column to compute grouped means for.
        """
        super().__init__(widget)
        self.groupby_col = groupby_col
        self.mean_col = mean_col

        # Put any other bookkeeping class variables you need here...
        self.groupby_sum = None
        self.groupby_count = None

    def process_slice(self, df_slice: pd.DataFrame) -> None:
        """
            Update the running grouped means with a dataframe slice.
        """
        # Implement me!
        group_by_df_slice = df_slice.loc[:,[self.groupby_col, self.mean_col]].groupby(self.groupby_col)
        if self.groupby_sum is None and self.groupby_count is None:
            self.groupby_sum = group_by_df_slice.sum()
            self.groupby_count = group_by_df_slice.count()
        else:
            self.groupby_sum = self.groupby_sum.combine(group_by_df_slice.sum(), lambda x1, x2: x1 + x2, fill_value=0)
            self.groupby_count = self.groupby_count.combine(group_by_df_slice.count(), lambda x1, x2: x1 + x2, fill_value=0)
        # print(self.groupby_sum)
        # print(self.groupby_count)
        # print(self.groupby_sum/self.groupby_count)

        # Update the plot
        # hint: self.update_widget(*list of groups*, *list of estimated group means of mean_col*)
        self.update_widget(self.groupby_sum.index.tolist(), (self.groupby_sum / self.groupby_count)[self.mean_col].tolist())


class GroupBySumOla(OLA):
    def __init__(self, widget: go.FigureWidget, original_df_num_rows: int, groupby_col: str, sum_col: str):
        """
            Class for performing OLA by incrementally computing the estimated grouped sums of *sum_col*
            with *groupby_col* as groups.

            @param original_df_num_rows: number of rows in the original dataframe before sampling and slicing.
            @param groupby_col: grouping column, i.e., df.groupby(groupby_col).
            @param sum_col: column to compute grouped sums for.
        """
        super().__init__(widget)
        self.original_df_num_rows = original_df_num_rows
        self.groupby_col = groupby_col
        self.sum_col = sum_col

        # Put any other bookkeeping class variables you need here...
        self.accum_len = 0
        self.groupby_sum = None

    def process_slice(self, df_slice: pd.DataFrame) -> None:
        """
            Update the running grouped sums with a dataframe slice.
        """
        # Implement me!
        self.accum_len += len(df_slice)
        group_by_df_slice = df_slice.loc[:,[self.groupby_col, self.sum_col]].groupby(self.groupby_col)
        if self.groupby_sum is None:
            self.groupby_sum = group_by_df_slice.sum()
        else:
            self.groupby_sum = self.groupby_sum.combine(group_by_df_slice.sum(), lambda x1, x2: x1 + x2)
        multiplier = self.original_df_num_rows/self.accum_len

        # Update the plot
        # hint: self.update_widget(*list of groups*, *list of estimated grouped sums of sum_col*)
        self.update_widget(self.groupby_sum.index.tolist(), [element * multiplier for element in self.groupby_sum[self.sum_col].tolist()])

class GroupByCountOla(OLA):
    def __init__(self, widget: go.FigureWidget, original_df_num_rows: int, groupby_col: str, count_col: str):
        """
            Class for performing OLA by incrementally computing the estimated grouped non-null counts in *count_col*
            with *groupby_col* as groups.

            @param original_df_num_rows: number of rows in the original dataframe before sampling and slicing.
            @param groupby_col: grouping column, i.e., df.groupby(groupby_col).
            @param count_col: counting column.
        """
        super().__init__(widget)
        self.original_df_num_rows = original_df_num_rows
        self.groupby_col = groupby_col
        self.count_col = count_col

        # Put any other bookkeeping class variables you need here...
        self.accum_len = 0
        self.groupby_count = None

    def process_slice(self, df_slice: pd.DataFrame) -> None:
        """
            Update the running grouped counts with a dataframe slice.
        """
        # Implement me!
        self.accum_len += len(df_slice)
        group_by_df_slice = df_slice.loc[:,[self.groupby_col, self.count_col]].groupby(self.groupby_col)
        if self.groupby_count is None:
            self.groupby_count = group_by_df_slice.count()
        else:
            self.groupby_count = self.groupby_count.combine(group_by_df_slice.count(), lambda x1, x2: x1 + x2, fill_value=0)
        multiplier = self.original_df_num_rows/self.accum_len

        # Update the plot
        # hint: self.update_widget(*list of groups*, *list of estimated group counts of count_col*)
        self.update_widget(self.groupby_count.index.tolist(), [element * multiplier for element in self.groupby_count[self.count_col].tolist()])


class FilterDistinctOla(OLA):
    def __init__(self, widget: go.FigureWidget, filter_col: str, filter_value: Any, distinct_col: str):
        """
            Class for performing OLA by incrementally computing the estimated cardinality (distinct elements) *distinct_col*
            where *filter_col* is equal to *filter_value*.

            @param filter_col: column to filter on.
            @param filter_value: value to filter for, i.e., df[df[filter_col] == filter_value].
            @param distinct_col: column to compute cardinality for.
        """
        super().__init__(widget)
        self.filter_col = filter_col
        self.filter_value = filter_value
        self.distinct_col = distinct_col

        # HLL for estimating cardinality. Don't modify the parameters; the autograder relies on it.
        # IMPORTANT: Please convert your data to the String type before adding to the HLL, i.e., self.hll.add(str(data))
        self.hll = HyperLogLog(p=2, seed=123456789)

        # Put any other bookkeeping class variables you need here...

    def process_slice(self, df_slice: pd.DataFrame) -> None:
        """
            Update the running filtered cardinality with a dataframe slice.
        """
        # Implement me!
        df_slice = df_slice[df_slice[self.filter_col]==self.filter_value]
        for data in df_slice[self.distinct_col].tolist():
            self.hll.add(str(data))
        

        # Update the plot. The filtered cardinality should be put into a singleton list due to Plotly semantics.
        # hint: self.update_widget([""], *estimated filtered cardinality of distinct_col*)
        self.update_widget([""], [self.hll.cardinality()])
