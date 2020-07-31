test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assign_color("HE_CLEAN") == "red"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assign_color("ILLDUMP") == "blue"
          True
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> assign_color("PARKS") == "green"
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
