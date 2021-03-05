import check50
import check50.c

@check50.check()
def exists():
  """question3-b exists"""
  check50.exists("question3-b.c")

@check50.check(exists)
def compiles():
  """question3-b compiles"""
  check50.c.compile("question3-b.c")

@check50.check(compiles)
def question3a():
  """question3-b runs"""
  check50.run("./question3-b").stdin("3\nsix seven eight", prompt=False).stdout("eight\nseven\nsix").exit(0)
