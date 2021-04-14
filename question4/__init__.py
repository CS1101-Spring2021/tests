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
    check50.run("./question4").stdin("ab+cd-*ef-/", prompt=False).stdout("a\na -> b\n(a + b)\n(a + b) -> c\n(a + b) -> c -> d\n(a + b) -> (c - d)\n((a + b) * (c - d))\n((a + b) * (c - d)) -> e\n((a + b) * (c - d)) -> e -> f\n((a + b) * (c - d)) -> (e - f)\n(((a + b) * (c - d)) / (e - f))\n", regex=True).exit(0)
