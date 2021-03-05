import check50
import check50.c

@check50.check()
def compiles():
  """question2-a compiles"""
  check50.c.compile("question2-a.c")
  
@check50.check(compiles)
def question2a():
  """question2-a runs"""
  check50.run("./question2-a").stdin("54 42", prompt=False).stdout("6\n").exit(0)
