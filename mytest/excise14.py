# 类定义
import datetime


class Golem:
  """docstring for ClassName"""

  def __init__(self, name=None):
    self.name = name
    self.built_year = datetime.date.today().year

  def say_hi(self):
    print('Hi!')


g = Golem('Clay')
g.name
g.built_year
g.say_hi()
g.say_hi

# inheritance


class Running_Golem(Golem):
  """docstring for Running_Golem"""

  def run(self):
    print("I'm running")
