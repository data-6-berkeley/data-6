test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> port_ozone == 0.03
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.round(port_tox_release, 2) == 325.56
          True
          """,
          'hidden': True,
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
