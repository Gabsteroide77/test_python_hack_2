"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    
    while True:
        if len(result) > 3:
            while True:
                if result == "fooziman":
                    x = result[2].replace(result[2] , "-")
                    y = result[7].replace(result[7] , "-")
                    return result[:2] + x + result[3:5] + "-" + result[5:7] + y
                elif result == "barziman":
                    x = result[2].replace(result[2] , "-")
                    y = result[5].replace(result[5] , "-")
                    return result[:2] + x + result[3:5] + y + result[6:8]
                break
        elif len(result) == 3:
            x = result[2].replace(result[2], "-")
            return result[:2] + x
        elif len(result) < 3:
            return result
        break
    return result
