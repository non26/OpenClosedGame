import re

def test_match(string):
    # compileObj = re.compile(r"\A(?=\w{3}\Z)(?=[^CO]{2}[CO])(?=[^0-4][0-4])")
    compileObj = re.compile(r"^([CO]{2}[0-4])$")
    matchObj = compileObj.match(string)
    return matchObj

print(bool(test_match("COdew")))
print(bool(test_match("CC444")))
print(bool(test_match("OO0")))
print(bool(test_match("OC1")))
if test_match("CC5"):
    print(test_match("CC5"))
else:
    print(test_match("CC5"))