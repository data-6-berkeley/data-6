test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(name_and_accel) == Table 
          True
          >>> name_and_accel.column("Acceleration").item(0) == 7.46
          True
          >>> name_and_accel.column("Vehicle Name").item(9) == 'Civic'
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
