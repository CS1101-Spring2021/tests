import check50
from re import match


# Question3 Checks
q3_test_str1 = "72 435 6 39 230 7 90"
q3_expected1 = "6, 7, 39, 72, 90, 230, 435"


@check50.check()
def q3_exists():
    """Does q3 exist?"""
    check50.exists("question3.py")


@check50.check(q3_exists)
def q3_check_test1():
    """Test with num list and check for sorted output string"""
    actual = check50.run("python3 question3.py").stdin(
        q3_test_str1, prompt=False).stdout()

    helptxt = ""
    if match(f"{q3_expected1}, ", actual):
        helptxt = "Did you add an extra comma (,) and a space to the end of tyour output string?"
    if not match(q3_expected1, actual):
        raise check50.Mismatch(q3_expected1, actual, help=helptxt)
