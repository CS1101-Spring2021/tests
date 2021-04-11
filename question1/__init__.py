import check50
import check50.c


@check50.check()
def exists():
    """question1 exists"""
    check50.exists("question1.c")


@check50.check(exists)
def compiles():
    """question1 compiles"""
    check50.c.compile("question1.c")


@check50.check(compiles)
def question1():
    """question1 runs"""
    check50.run("./question1").stdin("6").stdin("1\napple").stdin("1\norange").stdin("2").stdout("apple -> orange").stdin(
        "1\nbanana").stdin("1\nmelon").stdin("2").stdout("apple -> banana -> melon -> orange").exit(0)
