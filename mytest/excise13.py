
def _is_leap(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(_is_leap(200))
