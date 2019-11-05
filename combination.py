import re

def compare(s):

    patterns = {}

    patterns["Python"] = {
        "pattern": re.compile(r'''(python|Python|PYthon|PYThon|PYTHon|PYTHOn|PYTHON) $''', re.VERBOSE),
    }

    for x in patterns:

        pattern = patterns[x]["pattern"]
        m = pattern.match(s)

        if m:
            a = "Correct"
            d = {"Word correct": x,"Word passed": s}

            return a,d

        else:
            a = "Wrong"
            d = {"Word correct": x,"Word passed": s}

            return a,d

if __name__ == "__main__":

    print(compare("ALLALAL"))