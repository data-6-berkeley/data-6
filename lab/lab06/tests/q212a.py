test = {
    "name": "Question 2.1.2a.",
    "points": 1,
    "hidden": False,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import numpy as np
                    >>> np.isclose(avg_ucla_percent_change, np.average(((ucla_2019 - ucla_2009)/ucla_2009)*100))
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                }, 
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }, 
    ]
}