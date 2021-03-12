import check50
import check50.c


@check50.check()
def exists():
    """question2 exists"""
    check50.exists("question1.c")


@check50.check(exists)
def compiles():
    """question2 compiles"""
    check50.c.compile("question2.c")


@check50.check(compiles)
def question2():
    """question2 runs"""
    check50.run("./question2").exit(0)
