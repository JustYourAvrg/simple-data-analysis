# Data Visualization Dashboard

This repository contains a Python script that creates a data visualization dashboard using Dash and Plotly libraries. The dashboard allows you to visualize different aspects of a dataset through various interactive graphs.

## Dependencies

Before running the code, ensure that you have the following libraries installed:

- pandas
- plotly.express
- dash_bootstrap_components
- matplotlib
- plotly.graph_objects
- Flask
- dash
- dash_table
- dash_core_components
- dash_html_components
- dash.dependencies
- flask_session

You can install these dependencies using pip:
pip install pandas plotly dash dash_bootstrap_components matplotlib flask flask_session

## Usage

1. Clone this repository to your local machine.

2. Run the following command to start the Flask server:
python main.py

3. Open your web browser and go to `http://127.0.0.1:8050/dash/` to access the dashboard.

## Features

The data visualization dashboard provides the following features:

- Interactive selection of the dataset column to be plotted on the y-axis.
- Dropdown to choose the type of graph (heatmap, bar graph, scatter plot, line graph, box plot, violin plot, strip plot, histogram, pie chart, treemap).
- Dropdown to select the dataset column to be plotted on the x-axis.
- Display of the dataset in a paginated table format.

## How to Use

1. Choose the column you want to plot on the y-axis by selecting from the provided radio items.

2. Select the type of graph you want to visualize from the dropdown menu.

3. Choose the column you want to plot on the x-axis from the second dropdown menu.

4. The graph will automatically update based on your selections.

## Dataset

The code uses the Gapminder dataset for demonstration purposes. The dataset is loaded from the following URL:
https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv

You can replace this dataset with your own data by modifying the `data_path` variable in the script.

## Note

This code is intended for educational purposes and can be used as a starting point to build more complex data visualization dashboards using Dash and Plotly.

## Acknowledgments

The code is inspired by various Dash and Plotly examples and tutorials available in the community. Special thanks to the developers of Dash, Plotly, and Flask for providing excellent libraries for interactive data visualization in Python.

