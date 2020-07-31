test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> requests.num_rows == 8
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> requests.column(1).item(2) == 1265
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
