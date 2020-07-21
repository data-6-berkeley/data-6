test = {
  'name': 'Question 3_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(prop_votes_rounded) == 54
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.round(sum(prop_votes_rounded), 2) == 22.74
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
