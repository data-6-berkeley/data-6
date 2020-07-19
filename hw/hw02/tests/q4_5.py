test = {
  'name': 'Question 4_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like there may be an issue with your rounding or subtraction.
          >>> sum(usd_actual_prices) != 5442.0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(usd_actual_prices)
          12645.0
          >>> len(usd_actual_prices)
          167
          >>> usd_actual_prices.item(50)
          64.0
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
