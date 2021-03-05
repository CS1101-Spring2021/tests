import check50
import check50.c

@check50.check()
def exists():
  """question3-a exists"""
  check50.exists("question3-a.c")

@check50.check(exists)
def compiles():
  """question3-a compiles"""
  check50.c.compile("question3-a.c")

@check50.check(compiles)
def question3a():
  """question3-a runs"""
  check50.run("./question3-a").stdout("chocolate\nmelody\nsprite").exit(0)
