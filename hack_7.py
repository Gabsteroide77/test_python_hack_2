"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""

def fn_hack_7(s):
    result = s
    _ls = []

    if len(result) == 1:
        return result

    for i in range(1, len(result) + 1):
        if i % 2 == 0:
            _ls.append(i)
        else:
            _ls.append(str(i))

    return _ls