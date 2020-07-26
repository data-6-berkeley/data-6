test = {
  'name': 'Question 1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> port_tracts.num_rows == 757
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(port_tracts.column("ces_pollution_score")) == 18197.29
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> port_tracts.column("poverty").item(26) == 5.6
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
