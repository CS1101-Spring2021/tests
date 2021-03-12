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
def question4found():
  """missing number works"""
  check50.run("./question4").stdin("10\n49 40 26 34 16 35 19 14 17 3\n2", prompt=False).stdout("2 not found. 10 comparisons made.\n").exit(0)

@check50.check(question4found)
def question4notfound():
  """existing number works"""
  check50.run("./question4").stdin("10\n49 40 26 34 16 35 19 14 17 3\n19", prompt=False).stdout("19 found. 7 comparisons made.\n").exit(0)
