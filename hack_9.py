"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(s):
  result = s
  _ls = {}

  for i, value in result.items():
    if i == "foo":
      _ls["Foo"] = value.capitalize().replace("k","")
      
  return _ls