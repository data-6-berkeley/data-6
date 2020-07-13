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
          >>> np.sum(np.abs(population_in_billions_rounded - np.round(population / 1000000000, 2))) < .02
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
