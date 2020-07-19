test = {
  'name': 'Question 2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ca_presidential.column(1) == 14060856
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> ca_presidential.num_rows == 5
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> ca_presidential.column(0).item(3) == "gloria la riva"
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
