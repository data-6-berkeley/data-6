test = {
  'name': 'Question 3_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cand_per_state.num_rows == 51
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cand_per_state.labels[1]
          'number of candidates'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(cand_per_state.column(1)) == 3740
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
