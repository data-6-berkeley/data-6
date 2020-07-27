test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(june_states) == 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> june_states.item(4) == "Massachusetts"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> june_states.item(0) == "New York"
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
