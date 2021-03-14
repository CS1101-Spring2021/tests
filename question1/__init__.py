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
    check50.run("./question1").stdin("4").stdout("1) add at beginning\n2) add at end\n3) add after a particular node\n4) delete at beginning\n5) delete at end\n6) delete a particular node\n7) search a value\n8) traverse and display whole list\n").stdin("1\napple").stdin("1\norange").stdin("2\npear").stdin("8").stdout("orange -> apple -> pear -> \n").exit(0)

