test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like your result is an array, but it should be a single
          >>> # number.
          >>> import numpy as np
          >>> type(average_world_population) == np.float64 or type(average_world_population) == float
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your result isn't the right number.
          >>> round(average_world_population) == 4740454069.0
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
