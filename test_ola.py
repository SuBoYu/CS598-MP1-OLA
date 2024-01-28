from ola import FilterAvgOla, FilterDistinctOla, GroupByAvgOla, GroupByCountOla, GroupBySumOla
from utils import generate_plot, sample_split_df

from pympler import asizeof

import pandas as pd
import pickle

"""
***********************************************************************
* Please do not modify the test cases or the expected_results folder. *
***********************************************************************
"""


def test_ola_filter_avg():
    df = pd.read_csv("sales_train.csv")
    df_list = sample_split_df(df)
    widget = generate_plot("", "", "")
    ola = FilterAvgOla(widget, "item_id", 22154, "item_price")

    expected_keys = pickle.load(open("expected_results/filter_avg_key_list.pkl", "rb"))
    expected_vals = pickle.load(open("expected_results/filter_avg_val_list.pkl", "rb"))

    for i in range(len(df_list)):
        ola.process_slice(df_list[i])

        assert widget.data[0]['x'] == expected_keys[i], "The keys of the plot are incorrect."
        assert widget.data[0]['y'] == expected_vals[i], "The values of the plot are incorrect."

        # The size of the OLA class should be bounded.
        obj_size = asizeof.asizeof(ola)
        assert obj_size < 1000000, f"The size of the intermediate data you are storing in FilterAvgOla ({obj_size / 1000000} MB) exceeds 1MB."


def test_ola_groupby_avg():
    df = pd.read_csv("sales_train.csv")
    df_list = sample_split_df(df)
    widget = generate_plot("", "", "")
    ola = GroupByAvgOla(widget, "date_block_num", "item_cnt_day")

    expected_keys = pickle.load(open("expected_results/group_by_avg_key_list.pkl", "rb"))
    expected_vals = pickle.load(open("expected_results/group_by_avg_val_list.pkl", "rb"))

    for i in range(len(df_list)):
        ola.process_slice(df_list[i])

        assert (widget.data[0]['x'] == expected_keys[i]).all(), "The keys of the plot are incorrect."
        assert (widget.data[0]['y'] == expected_vals[i]).all(), "The values of the plot are incorrect."

        # The size of the OLA class should be bounded.
        obj_size = asizeof.asizeof(ola)
        assert obj_size < 1000000, f"The size of the intermediate data you are storing in GroupByAvgOla ({obj_size / 1000000} MB) exceeds 1MB."


def test_ola_groupby_sum():
    df = pd.read_csv("sales_train.csv")
    df_list = sample_split_df(df)
    widget = generate_plot("", "", "")
    ola = GroupBySumOla(widget, len(df), "shop_id", "item_cnt_day")

    expected_keys = pickle.load(open("expected_results/group_by_sum_key_list.pkl", "rb"))
    expected_vals = pickle.load(open("expected_results/group_by_sum_val_list.pkl", "rb"))

    for i in range(len(df_list)):
        ola.process_slice(df_list[i])

        assert (widget.data[0]['x'] == expected_keys[i]).all(), "The keys of the plot are incorrect."
        assert (widget.data[0]['y'] == expected_vals[i]).all(), "The values of the plot are incorrect."

        # The size of the OLA class should be bounded.
        obj_size = asizeof.asizeof(ola)
        assert obj_size < 1000000, f"The size of the intermediate data you are storing in GroupBySumOla ({obj_size / 1000000} MB) exceeds 1MB."


def test_ola_groupby_count():
    df = pd.read_csv("sales_train.csv")
    df_list = sample_split_df(df)
    widget = generate_plot("", "", "")
    ola = GroupByCountOla(widget, len(df), "shop_id", "item_cnt_day")

    expected_keys = pickle.load(open("expected_results/group_by_count_key_list.pkl", "rb"))
    expected_vals = pickle.load(open("expected_results/group_by_count_val_list.pkl", "rb"))

    for i in range(len(df_list)):
        ola.process_slice(df_list[i])

        assert (widget.data[0]['x'] == expected_keys[i]).all(), "The keys of the plot are incorrect."
        assert (widget.data[0]['y'] == expected_vals[i]).all(), "The values of the plot are incorrect."

        # The size of the OLA class should be bounded.
        obj_size = asizeof.asizeof(ola)
        assert obj_size < 1000000, f"The size of the intermediate data you are storing in GroupByCountOla ({obj_size / 1000000} MB) exceeds 1MB."


def test_ola_filter_distinct():
    df = pd.read_csv("sales_train.csv")
    df_list = sample_split_df(df)
    widget = generate_plot("", "", "")
    ola = FilterDistinctOla(widget, "shop_id", 10, "item_id")

    expected_keys = pickle.load(open("expected_results/filter_distinct_key_list.pkl", "rb"))
    expected_vals = pickle.load(open("expected_results/filter_distinct_val_list.pkl", "rb"))

    for i in range(len(df_list)):
        ola.process_slice(df_list[i])

        assert widget.data[0]['x'] == expected_keys[i], "The keys of the plot are incorrect."
        assert widget.data[0]['y'] == expected_vals[i], "The values of the plot are incorrect."

        # The size of the OLA class should be bounded.
        obj_size = asizeof.asizeof(ola)
        assert obj_size < 1000000, f"The size of the intermediate data you are storing in FilterDistinctOla ({obj_size / 1000000} MB) exceeds 1MB."
