import matplotlib
import matplotlib.pyplot as plots
from datascience import *
import numpy as np
Table.interactive_plots()

def avg_percent_change(arr09, arr19):
    amount_change = arr19 - arr09
    original_amount = arr09
    return np.average(100 * (amount_change / original_amount))

def draw_bar_plot(categories_label, categories, values_label, values):
    Table().with_column(categories_label, categories)\
        .with_column(values_label, values).barh(categories_label)

def draw_group_barh(title, data):
  """Draws a bar chart of the unique values in the given array
  
  Args:
  - title (str): A title for the chart.
  - data (array): An array of values.  Repeated values are counted
      and given larger bars in the resulting chart.
      
  """
  Table().with_column(title, data).group(title).sort(1, descending = True).barh(title)

def draw_line_plot(x_label, x_data, y_label, y_data):
    """Draws a line plot of the given data.
    
    Args:
    - x_label (str): The horizontal axis label.
    - x_data (array): The horizontal ("x") values of the points
        that are connected to form the plot.
    - y_label (str): The vertical axis label.
    - y_data (array): The vertical ("y") values of the points that
        are connected to form the plot.
    """
    Table().with_columns(x_label, x_data, y_label, y_data).plot(x_label)

def draw_scatter_plot(x_label, x_data, y_label, y_data):
    """Draws a scatter plot of the given data.
    
    Args:
    - x_label (str): The horizontal axis label.
    - x_data (array): The horizontal ("x") values of the points
        in the plot.
    - y_label (str): The vertical axis label.
    - y_data (array): The vertical ("y") values of the points in
        the plot.
    """
    Table().with_columns(x_label, x_data, y_label, y_data).scatter(x_label)

def load_and_clean_table(url):
    """Loads a table about Marvel or DC comics from fivethirtyeight's
    GitHub repository, and cleans up a few formatting details."""
    tbl = Table.read_table(url)
    if "Year" in tbl.labels:
        tbl.relabel("Year", "YEAR")
        tbl.update({'PUBLISHER': 'Marvel'})
    else:
        tbl.update({'PUBLISHER': 'DC'})
    tbl.relabel("name", "NAME")
    tbl.update({"APPEARANCES": np.nan_to_num(tbl.column("APPEARANCES"))})
    tbl.update({"GENDER": np.char.replace(tbl.column("SEX"), "nan", "Unknown")})
    tbl.update({"GENDER": np.char.replace(tbl.column("GENDER"), " Characters", "")})
    
    def extract_month(date_text):
        import dateutil.parser
        try:
            return dateutil.parser.parse(date_text).month
        except:
            return "Unknown"
    
    tbl.update({"MONTH": tbl.apply(extract_month, "FIRST APPEARANCE")})
    tbl.update({"MONTH": tbl.apply(lambda d: int(d) if d != "Unknown" else -1, "MONTH")})
    tbl = tbl.select("PUBLISHER", "NAME", "GENDER", "APPEARANCES", "YEAR", "MONTH")
    for l in tbl.labels:
        tbl.relabel(l, l.capitalize())
    tbl = tbl.where(~np.isnan(tbl.column("Year")))
    return tbl