"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(s):
    result = s
    _ls = []
    x = reversed(range(len(result)))
    if len(result) % 2 == 0:
        for item in x:
            _ls.append(str(item + 1))
    else:
        for i in x:
            _ls.append(result[i] + "-" + str(i + 1))
    return _ls
