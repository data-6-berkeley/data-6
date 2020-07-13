import matplotlib
import matplotlib.pyplot as plots
from datascience import *
import numpy as np
Table.interactive_plots()

def draw_group_barh(title, data):
    """Draws a bar chart of the unique values in the given array. 
    Args:
    - title (str): A title for the chart.
    - data (array): An array of values.  Repeated values are counted
      and given larger bars in the resulting chart.
    """
    Table().with_column(title, data).group(title).sort(1, descending = True).barh(title)

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
