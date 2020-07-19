test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> vehicles.item(0) == 'Prius (1st Gen)'
          True
          >>> year.item(1) == 2000
          True
          >>> mpg.item(2) == 45.23
          True
          >>> msrp.item(3) == 18936.41
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
