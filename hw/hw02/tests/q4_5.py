test = {
  'name': 'Question 4_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like there may be an issue with your rounding or subtraction.
          >>> sum(price_difference) == 5442.0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(price_difference)
          5442.0
          >>> len(price_difference)
          167
          >>> price_difference.item(50)
          36.0
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
