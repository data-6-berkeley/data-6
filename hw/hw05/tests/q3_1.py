test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> population.num_rows == 106450
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> population.column(0).item(99001) == 'Neither support nor oppose'
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
