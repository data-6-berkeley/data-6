test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(acceleration) == np.ndarray
          True
          >>> type(acceleration[0]) == np.float64
          True
          >>> acceleration[1] == 8.2
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
