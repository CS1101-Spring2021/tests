import check50
import check50.c


@check50.check()
def exists():
    """question2 exists"""
    check50.exists("question2.c")


@check50.check(exists)
def compiles():
    """question2 compiles"""
    check50.c.compile("question2.c")


@check50.check(compiles)
def question2():
    """question2 runs"""
    check50.run("./question2").stdin("13").stdin("5").stdout("1").stdin("1\napple").stdin(
        "1\norange").stdin("6").stdout("orange\napple").stdin("2").stdout("orange").stdin(
            "3").stdout("apple").stdin("2").stdout("apple").stdin("3").stdout("-1").stdin(
                "1\nsparrow").stdout("1\npigeon").stdin("4").stdout("0").stdin("1\ncrow").stdin(
                    "3").stdout("crow").stdin("6").stdout("crow\npigeon\nsparrow").exit(0)
