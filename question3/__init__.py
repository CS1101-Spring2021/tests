import check50
import check50.c


@check50.check()
def exists():
    """question3 exists"""
    check50.exists("question3.c")


@check50.check(exists)
def compiles():
    """question3 compiles"""
    check50.c.compile("question3.c")


@check50.check(compiles)
def question3():
    """question3 runs"""
    check50.run("./question3").stdin("4", prompt=False).stdout("N> ").stdin("16", prompt=False).stdin("6").stdout("1").stdin("1\napple").stdin(
        "1\norange").stdin("1\nbanana").stdin("7").stdout("apple -> orange -> banana").stdin(
            "3").stdout("apple").stdin("4").stdout("banana").stdin("2").stdin("1\nmelon").stdin(
                "3").stdout("orange").stdin("1\npigeon").stdin("5").stdin("5").stdout("1").stdin(
                    "2").stdin("5").stdout("0").stdin("1\nparrot").stdin("7").stdout(
                        "banana -> melon -> pigeon -> parrot").exit(0)