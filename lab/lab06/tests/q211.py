test = {
    "name": "Question 2.1.1.",
    "points": 1,
    "hidden": False,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import numpy as np
                    >>> type(berkeley_2019) == np.ndarray and type(berkeley_amount_change) == np.ndarray
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                }, 
                {
                    "code": r"""
                    >>> import numpy as np
                    >>> np.isclose(avg_berkeley_percent_change, 144.541)
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