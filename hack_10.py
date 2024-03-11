"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(s):
  result = s
  _ls = []

  if len(result) == 1:
    return result

  for i in range(1, len(result) * 2, 2):
    if i % 2 == 0:
        _ls.append(str(i))
    else:
        _ls.append({str(i): str(i + 1)})

  return _ls