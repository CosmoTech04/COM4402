
def group_marks(marks):

 if not isinstance(marks, list):
  raise TypeError("marks must be a list")

 grade = {
  "Fail": [],
  "Pass": [],
  "Distinction": []
 }

 for mark in marks:
  if not isinstance(mark, int):
   raise TypeError("each mark must be an integer")

  if mark < 0 or mark > 100:
   raise ValueError("marks must be between 0 and 100")

  if mark < 40:
   grade["Fail"].append(mark)
  elif 40 <= mark < 70:
   grade["Pass"].append(mark)
  else:
   grade["Distinction"].append(mark)

 return grade
