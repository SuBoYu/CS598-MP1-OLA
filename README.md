# Project 1
CS 598 YP Spring 2024\
**Last Updated:** January 30th 2024\
**Deadline:** February 27th 2024, 11:59 PM CT

## Project Overview
In this project, you will be implementing Online Aggregation (OLA) for a few basic operations in Pandas.
You will observing OLA in action with dynamically updating Plotly plots, which will display incrementally improving estimates alongside the processing of the dataframe.

## Getting Started
To get started, you will need to [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository to your own Github account - please do not commit directly to this repository!
You will then need to make your cloned repository **private**. To do so, navigate to the "Change repository visibility" setting in the "Settings" tab:

<img width="855" alt="Screenshot 2024-01-30 at 1 35 16 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/db0cba69-642f-40bb-b6ac-6d407ff64414">

<img width="789" alt="Screenshot 2024-01-30 at 1 35 22 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/e96c4476-cd1a-41b3-a77b-46471d38ebce">

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

You can find the skeleton code for each operation in the child classes of the base `Ola` class (e.g., `GroupByAvgOla`). **An implementation of computing mean with OLA (i.e., `avg(x)`) is provided to you as an example in the [`AvgOla`](https://github.com/illinoisdata/CS598-MP1-OLA/blob/main/ola.py#L38) class.**
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

You can check your assignment progress via the Github Actions workflow (described below). If the actions workflow passes, you will receive full score for this assignment. 

You should not modify `utils.py`, `test_ola.py` or the `expected_results` directory as they are used by the autograder.

## Accessing Github Actions
Github Actions can be accessed by clicking in the location specified in the image below: it currently displays a red X because the tests are failing (as nothing has been implemented yet).

<img width="917" alt="Screenshot 2024-01-30 at 1 24 04 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/e77908ba-77b2-4ac3-ad64-4d5409117a45">

You can check which test cases have passed or failed by clicking on the details tab:

<img width="644" alt="Screenshot 2024-01-30 at 1 24 13 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/73a89793-b45e-4513-a57c-a31928627774">

<img width="1123" alt="Screenshot 2024-01-30 at 1 24 24 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/42ab4199-809e-48e7-bf4a-5b36bca26fcb">

A full-score submission with a passing Github Actions workflow looks like this:

<img width="362" alt="Screenshot 2024-01-30 at 1 24 43 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/be61179a-9d30-43cb-80b8-6178524a4d05">

<img width="714" alt="Screenshot 2024-01-30 at 1 24 53 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/7471d8e3-c22e-40bc-b826-a5e88fbbcaaf">

## Submission instructions

You will submit your work for Project 1 by uploading the URL of your private repository to the Project 1 - OLA assignment to Canvas. You will also need to share access to your private repository to the two course TAs:
- Billy Li (BillyZhaohengLi)
- Hanxi Fang (iq180fq200)

You can share access by navigating to Settings -> Collaborators:

<img width="372" alt="Screenshot 2024-01-30 at 1 35 36 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/f4670e71-2e68-4acc-9baa-b669dca0eace">
<img width="785" alt="Screenshot 2024-01-30 at 1 35 42 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/80162427-a380-49a2-8257-70f357225994">
<img width="622" alt="Screenshot 2024-01-30 at 1 39 33 PM" src="https://github.com/illinoisdata/CS598-MP1-OLA/assets/31910858/4741b598-35ae-4c50-9733-d6508cbfa64b">
