test = {
  'name': '1.1.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Fill in the line
          >>> #   smaller_distance = ...
          >>> # in the cell above.
          >>> smaller_distance != ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Remember that it takes an additional 1000 meters to get 
          >>> # to the portal.
          >>> num_avenues_away != 274
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Remember that there is an extra distance to walk after 
          >>> # the 1000 meters.
          >>> num_avenues_away != 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> smaller_distance == 1274
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
