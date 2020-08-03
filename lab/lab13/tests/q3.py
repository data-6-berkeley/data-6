test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sample_prob_tbl.num_columns == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sample_prob_tbl.num_rows == 5 or sample_prob_tbl.num_rows == 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.round(sum(sample_prob_tbl.column(1))) == 1.0
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
