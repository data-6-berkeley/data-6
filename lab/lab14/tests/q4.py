test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(convenience_stats)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(convenience_stats[0]), 2) == 101924.46
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(convenience_stats[1]), 2) == 53180.55
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
