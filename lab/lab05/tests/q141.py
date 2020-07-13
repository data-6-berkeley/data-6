test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer isn't quite right, or it's not an array.
          >>> import numpy as np
          >>> np.sum(np.abs(population_in_billions - population / 1000000000)) < .001
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
