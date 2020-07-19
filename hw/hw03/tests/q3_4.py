test = {
  'name': 'Question 3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hrc_votes.num_rows == 54
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> hrc_votes.column(0).item(0) == 2016
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(hrc_votes.column("candidatevotes")) == 65853581
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
