test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(hybrids) == Table
          True
          >>> hybrids.num_rows == 153
          True
          >>> hybrids.select("vehicle", "year", "msrp", "acceleration", "mpg").sort(0).take(range(5))
          vehicle        | year | msrp    | acceleration | mpg
          3008           | 2011 | 45101.5 | 11.36        | 61.16
          A5 BSG         | 2009 | 11849.4 | 7.87         | 35.28
          Accord         | 2005 | 16343.7 | 14.93        | 28
          ActiveHybrid 3 | 2013 | 49650   | 14.93        | 28
          ActiveHybrid 5 | 2012 | 62180.2 | 16.67        | 26
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
