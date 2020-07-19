test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(ca_candidates.column(1)) == 13716098
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> ca_candidates.column(0).item(2) == "gary johnson"
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
