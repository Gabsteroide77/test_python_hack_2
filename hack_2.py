"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

def fn_hack_2(s):
  result = s
  vocales = ["a","e","i","o","u"]
  _ls = []
  
  for texto in result:
    if texto not in vocales:
      _ls.append(texto)

  result = "".join(_ls)
  return result