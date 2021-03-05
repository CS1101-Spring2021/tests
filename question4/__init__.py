import check50
import check50.c

@check50.check()
def compiles():
  """question4 compiles"""
  check50.c.compile("question4.c")
  
@check50.check(compiles)
def question4found():
  """missing number works"""
  check50.run("./question4").stdin("10\n5 6 7 8 9 10 11 12 13 14\n4", prompt=False).stdout("4 not found. 4 comparisons made.\n").exit(0)
  
@check50.check(question4found)
def question4notfound():
  """existing number works"""
  check50.run("./question4").stdin("10\n5 6 7 8 9 10 11 12 13 14\n12", prompt=False).stdout("12 found. 2 comparisons made.\n").exit(0)
