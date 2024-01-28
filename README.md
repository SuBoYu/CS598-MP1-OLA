# Project 1 (Tentative, subject to change)
CS 598 YP Spring 2024\
**Last Updated:** January 26th 2024\
**Deadline:** February 27th 2024, 11:59 PM CT

## Project Overview
In this project, you will be implementing Online Aggregation (OLA) for a few basic operations in Pandas.
You will observing OLA in action with dynamically updating Plotly plots, which will display incrementally improving estimates alongside the processing of the dataframe.

## Getting Started
The goal of this project is to answer questions on the [Predict Future Sales](https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales) dataset (included in this repository as `sales_train.csv`) in OLA fashion.
The starter code for sampling the dataframe and dividing it into suitable-sized slices for incremental processing has been provided to you in `utils.py`. 
The visualization code is also provided to you in `Visualization.ipynb`.

## Tasks
Your task is to implement OLA for 5 different operations in `ola.py`: 

- Filtered mean, i.e., `avg(x) where y = z` (5 points)
- Grouped means, i.e., `avg(x) group by y`  (10 points)
- Grouped sums, i.e., `sum(x) group by y`  (10 points)
- Grouped counts, i.e., `count(x) group by y`  (10 points)
- Filtered cardinality [via HLL](https://github.com/AdRoll/python-hll) , i.e., `count_distinct(x) where y = z` (**Extra credit**, 5 points)

You can find the skeleton code for each operation in the child classes of the base `Ola` class (e.g., `GroupByAvgOla`). An implementation of computing mean with OLA (i.e., `avg(x)`) is provided to you as an example in the `AvgOla` class.
For each operation, you will implement the logic for processing incoming dataframe slices in the `process_slice` class function: 
when a new slice arrives, you will perform computations on the slice to improve your estimated values, then update the Plotly plot with the improved estimates.
You are also allowed to use limited amount of space for bookkeeping (e.g., storing rolling averages) in the form of class variables during the processing of subsequent slices.

You are only required to implement the OLA logic; there is no SQL parsing involved in this assignment.

## Verifying Your Results
You can verify your implementations of OLA operations with the `Visualization.ipynb` notebook. It contains 5 Plotly plots, one for each OLA operation. 
Once you correctly implement the OLA operations, you can click 'run all' to observe the Plotly plots dynamically updating with the processing of dataframe slices.

It is recommended that you run the notebook in a Jupyter Notebook session; The Plotly plots have been observed to fail in certain platforms/IDEs such as JupyterHub or PyCharm.
Running the notebook and observing the plot updates is **optional** for this assignment: you are not required to record the dynamic updates.

## Grading
You will be graded on the correctness of your implementations. You will receive the points for each operation if your implementation satisfies the following two criteria:
- The contents of the Plotly plots after each processed dataframe slice are correct
- The combined size of class variables you use for bookkeeping is smaller than a certain size during the OLA process (so no storing entire dataframes - that defeats the purpose of OLA)

You can check your assignment progress via the Github Actions workflow. If the actions workflow passes (i.e., shows a green checkmark), you will receive full score for this assignment.

You should not modify `utils.py`, `test_ola.py` or the `expected_results` directory as they are used by the autograder.
