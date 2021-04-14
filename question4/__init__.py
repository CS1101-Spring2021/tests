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
    check50.run("./question4").stdin("ab+cd-*ef-/", prompt=False).stdout("a[\s]?\na -> b\n(a + b)[\s]?\n(a + b) -> c[\s]?\n(a + b) -> c -> d[\s]?\n(a + b) -> (c - d)[\s]?\n((a + b) * (c - d))[\s]?\n((a + b) * (c - d)) -> e[\s]?\n((a + b) * (c - d)) -> e -> f[\s]?\n((a + b) * (c - d)) -> (e - f)[\s]?\n(((a + b) * (c - d)) / (e - f))[\s]?", regex=True).exit(0)
