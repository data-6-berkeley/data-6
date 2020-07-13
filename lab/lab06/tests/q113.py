test = {
    "name": "Question 1.1.3.",
    "points": 1,
    "hidden": False,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import numpy as np
                    >>> np.allclose(berkeley_in_thousands, berkeley_prices/1000)
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