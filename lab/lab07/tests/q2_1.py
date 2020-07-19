test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(ten_vehicles) == tables.Table
          True
          >>> ten_vehicles.select('Name', 'MPG').sort('MPG').column('MPG').item(0)
          40.46
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
