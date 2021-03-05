import check50
import check50.c

@check50.check()
def compiles()
  """question1 compiles"""
  check50.c.compile("question1.c")
  
@check50.check()
def question1()
  """question1 runs"""
  check50.run("./question1").stdin("15 5").stdout("5\n").exit(0)
