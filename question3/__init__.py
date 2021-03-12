import check50
import check50.c


@check50.check()
def exists():
    """question3 exists"""
    check50.exists("question1.c")


@check50.check(exists)
def compiles():
    """question3 compiles"""
    check50.c.compile("question3.c")


@check50.check(compiles)
def question3():
    """question3 runs"""
    check50.run("./question3").exit(0)
