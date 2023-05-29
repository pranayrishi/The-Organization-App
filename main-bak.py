
from replit import db
import datetime as dt
def AssignmentDueDate():
  HomeworkDueDateYear = int(input("Enter the year in which your assignment is due: "))
  HomeworkDueDateMonth = int(input("Enter the month in which your assignment is due: "))
  HomeworkDueDateDay = int(input("Enter the day in which your assignment is due: "))
  HomeworkDueDate = dt.date(HomeworkDueDateYear, HomeworkDueDateMonth, HomeworkDueDateDay)
  CurrentDate = dt.date.today()
  CurrentTime = dt.datetime.now
  db[AssignmentTitle] = AssignmentTitle
  db[AssignmentType] = AssignmentType
  db[HomeworkDueDateYear] = HomeworkDueDateYear
  db[HomeworkDueDateMonth] = HomeworkDueDateMonth
  db[HomeworkDueDateDay] = HomeworkDueDateDay
  

#General Information
StudentName = str(input("What is your name?: "))
StudentGrade = str(input("What is your grade level?: "))
StudentPeriodsOrClasses = int(input("How many classes or periods do you have homework for today? "))
db[StudentName] = StudentName
db[StudentGrade] = StudentGrade

#School-Work
for classes in range(0, StudentPeriodsOrClasses, 1):
  AssignmentTitle = str(input("What is your homework today?:"))
  AssignmentType = str(input("What type of assignment are you work on(ie: Homework, Quiz, Test, Project, or No Homework)?: "))
  AssignmentTypeChange = AssignmentType.upper()
  if AssignmentTypeChange == "HOMEWORK":
    print("Lets Finish This!!") #default: change later on
    AssignmentDueDate()
  elif AssignmentTypeChange == "TEST":
    print("GoodLuck!") #default: change later on
    AssignmentDueDate()
  elif AssignmentTypeChange == "QUIZ":
    print("GoodLuck!") #default: change later on
    AssignmentDueDate()
  elif AssignmentTypeChange == "PROJECT":
    print("GoodLuck!") #default: change later on
    AssignmentDueDate()
  elif AssignmentTypeChange == "NO HOMEWORK":
    print("Sad :(")  
  else:
    print("See if you made a mistake in your typing? Or pleaese be direct in your answer about your assignment type.")

#Extra-Cirricular Activites
ExtraCirricularActivities = int(input("How many extra-cirriculum actvities do you have today?: "))
for activities in range(0, ExtraCirricularActivities, 1):
  ExtraCirricularActivity = str(input("What are your extra-cirricular activites today?: "))
  ExtraCirricularTimeInHours = int(input("What time in hours is your extra-cirricular activites today?: "))
  ExtraCirricularTimeInMinutes = int(input("What time in minutes is your extra-cirricular activities today?:"))
  ExtraCirricularActivitiesTime = dt.time(ExtraCirricularTimeInHours, ExtraCirricularTimeInMinutes)
  db[ExtraCirricularActivity] = ExtraCirricularActivity
  db[ExtraCirricularTimeInHours] = ExtraCirricularTimeInHours
  db[ExtraCirricularTimeInMinutes] = ExtraCirricularTimeInMinutes
print("Thank You for this information! Now a schedule will be created for you!")
