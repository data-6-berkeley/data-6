from datascience import *
import numpy as np

def simulate_under_null(table):
    test_stats = make_array()
    for i in np.arange(1000):
        shuffled_labels = table.sample(with_replacement = False).column(0)
        shuffled_table = Table().with_columns("Treatment", shuffled_labels,
                                              "Interested in raising animals", table.column(1))
        grouped = shuffled_table.group(0, np.average)
        differences = abs(grouped.column(1).item(0) - grouped.column(1).item(1))
        test_stats = np.append(test_stats, differences)
    return test_stats

