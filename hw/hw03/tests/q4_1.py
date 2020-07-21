test = {
  'name': 'Question 4_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> parties.num_rows == 148
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> parties.labels[1]
          '# of times'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(parties.column(1)) == 3740
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
