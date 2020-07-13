test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you're not making an array.  You shouldn't need to
          >>> # use .item anywhere in your solution.  Just call np.diff on something.
          >>> import numpy as np
          >>> type(population_changes) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You made an array, but it doesn't have the right size.  It should
          >>> # have one element for each element of the population array, minus
          >>> # one, since there's no successor year to 2015 to compute the increase
          >>> # in that year.
          >>> import numpy as np
          >>> len(population_changes) == 65
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The numbers in your array aren't right.
          >>> import numpy as np
          >>> population_changes.item(0) == 37311223
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
