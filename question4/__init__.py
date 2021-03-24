import check50
import check50.c


@check50.check()
def exists():
    """question4 exists"""
    check50.exists("question4.c")


@check50.check(exists)
def compiles():
    """question4 compiles"""
    check50.c.compile("question4.c")


@check50.check(compiles)
def question4():
    """question4 runs"""
    check50.run("./question4").stdin("7").stdin("1\napple").stdin("1\norange").stdin(
        "2\npear").stdin("7\napple").stdout("1").stdin("7\norange").stdout("0").stdin("7\nbanana").stdout("-1").stdin("8").stdout("orange -> apple -> pear").exit(0)
