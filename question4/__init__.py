import check50
from re import match

# Question4 Checks


@check50.check()
def q4_exists():
    """Does q4 exist?"""
    check50.exists("question4.py")
    check50.include("q4.input", "q4.output")


@check50.check(q4_exists)
def q4_check_output():
    """Send paragraph to q4 and check output"""
    expected = open('q4.output').read()
    actual = check50.run("python3 question4.py").stdout()
    actual = str(actual)

    helptxt = "Check if you are missing any word from the output text placeholder."

    if expected != actual:
        raise check50.Mismatch(expected, actual, help=helptxt)
