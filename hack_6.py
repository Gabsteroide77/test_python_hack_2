"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
  result = s
  _ls = []

  for i in range(len(result)):
    if (i + 1) % 2 != 0:
        _ls.append(str(i + 1))
    else:
        _ls.append("-")

  if not _ls:
    _ls.append("0")

  return _ls