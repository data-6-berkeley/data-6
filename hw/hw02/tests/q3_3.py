test = {
  'name': 'Question 3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> # It looks like you didn't make an array.
          >>> type(go_bears) == np.ndarray
          True
          >>> # It looks like you included commas in the text.
          >>> # The three pieces of text in the array should be:
          >>> #   "Go"
          >>> #   "Bears"
          >>> #   "Beat Stanford!"
          >>> not any([',' in text for text in go_bears])
          True
          >>> # It looks like you didn't include both words or the exclamation mark
          >>> # in the last piece of text.  It should be the actual string:
          >>> #   "Beat Stanford!"
          >>> 'Beat ' in go_bears.item(2)
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
