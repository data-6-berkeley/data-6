test = {
  'name': 'Question 8_2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # There should be one pressure for each frame.
          >>> len(a_pressures) == len(frame_times)
          True
          >>> # You're on the right track, but the formula for pressure
          >>> # involves just a couple more numbers.
          >>> import numpy as np
          >>> not(all(a_pressures == np.sin(frame_times)))
          True
          >>> # You're on the right track, but the formula for pressure
          >>> # involves just a couple more numbers.
          >>> import numpy as np
          >>> not(all(a_pressures == np.sin(220*frame_times)))
          True
          >>> # You're on the right track, but the formula for pressure
          >>> # involves just a couple more numbers.
          >>> import numpy as np
          >>> not(all(a_pressures == np.sin(2*np.pi*frame_times)))
          True
          >>> "{:.4}".format(a_pressures[45])
          '0.9872'
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
