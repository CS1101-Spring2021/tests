import check50
from re import match


q2_test_str1 = "apple orange banana custard-apple pear guava"
# Question2 Checks


@check50.check()
def q2_exists():
    """Does q2 exist?"""
    check50.exists("question2.py")
    check50.include("q2.input", "q2.output")


@check50.check(q2_exists)
def q2_send_inputfile():
    """Send list to q2"""
    check50.run("python3 question2.py").stdin(
        q2_test_str1, prompt=False).exit(0)


@check50.check(q2_send_inputfile)
def q2_outputfile_exists():
    """Is the output file generated"""
    check50.exists("q2_output.txt")


@check50.check(q2_outputfile_exists)
def q2_read_outputfile1():
    """Output file has the replaced strings"""
    expected = open('q2.output').read().lower()
    actual = open('q2_output.txt').read().lower()

    helptext = ""
    if "\n" not in actual:
        helptext = "Did you forget the newlines after every list item?"

    if not match(expected, actual):
        raise check50.Mismatch(expected, actual, help=helptext)
