
import check50
import check50.c

@check50.check()
def compiles():
  """question2-b compiles"""
  check50.c.compile("question2-b.c")
  
@check50.check(compiles)
def question2b():
  """question2-b runs"""
  check50.run("./question2-b").stdin("54 42", prompt=False).stdout("[3-4]\n6\n", regex=True).exit(0)
