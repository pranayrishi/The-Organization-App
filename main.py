from replit import db
import datetime as dt
import random
import time 

def AssignmentDueDate(order):
  HomeworkDueDateYearInt = int(input("Enter the year in which your assignment is due: "))
  HomeworkDueDateMonthInt = int(input("Enter the month in which your assignment is due: "))
  HomeworkDueDateDayInt = int(input("Enter the day in which your assignment is due: "))
  db[AssignmentTitleStr] = AssignmentTitleStr
  db[AssignmentTypeStr] = AssignmentTypeStr
  db[HomeworkDueDateYearInt] = HomeworkDueDateYearInt
  db[HomeworkDueDateMonthInt] = HomeworkDueDateMonthInt
  db[HomeworkDueDateDayInt] = HomeworkDueDateDayInt
  MyDate = dt.datetime(HomeworkDueDateYearInt, HomeworkDueDateMonthInt, HomeworkDueDateDayInt)
  print("Assignment date is ==> ")
  print(MyDate)

def EncouragementWords():
  EncouragementWords = ["Stay On Task", "You can do this, just focus" "Life is like a bicycle. To keep your balance, you just keep moving.", "Persistence is very important. You should not GIVE UP unless you are forced to give up!", "You must stay focused on the end result to achieve your goals.", "Most people have no idea of the giant capacity we can immediately command when we focus all of our resources on mastering a single area of our lives.", "Whatever is difficult can be done with regular attention and actions. Stay focused."]
  time.sleep(1) #Edit here
  print(random.choice(EncouragementWords))

def MultipleEncouragementWords():
  for EncourageMentWords in range(1, 2, 1): #Edit here
    EncouragementWords()
  
#General Information
StudentNameStr = str(input("What is your name?: "))
StudentGradeStr = str(input("What is your grade level?: "))
StudentPeriodsOrClassesInt = int(input("How many classes or periods do you have homework for today? "))
StudentPeriodOrClassesStr = str(StudentPeriodsOrClassesInt)
db[StudentNameStr] = StudentNameStr
db[StudentGradeStr] = StudentGradeStr

#School-Work
for classes in range(0, StudentPeriodsOrClassesInt, 1):
  AssignmentTitleStr = str(input("What is your homework today?:"))
  AssignmentTypeStr = str(input("What type of assignment are you work on(ie: Homework, Quiz, Test, Project, or No Homework)?: "))
  AssignmentTypeChange = AssignmentTypeStr.upper()
  if AssignmentTypeChange == "HOMEWORK":
    print("Lets Finish This!!") #default: change later on
    HomeworkDescription = input("Please input your homework description (i.e. Google Classroom work or pg. 12 #1-12): ")
    AssignmentDueDate(classes)
  elif AssignmentTypeChange == "TEST":
    print("GoodLuck!") #default: change later on
    TestDescriptionStr = input("Please input what your test is about?: ")
    AssignmentDueDate(classes)
  elif AssignmentTypeChange == "QUIZ":
    print("GoodLuck!") #default: change later on
    QuizDescriptionStr = input("Please input what your quiz is about?: ")
    AssignmentDueDate(classes)
  elif AssignmentTypeChange == "PROJECT":
    print("GoodLuck!") #default: change later on
    ProjectDescriptionStr = input("Please input what your project is about: ")
    AssignmentDueDate(classes)
  elif AssignmentTypeChange == "NO HOMEWORK":
    print("Sad :(") 
    print("If you have no other homework, try reading a book for fun or excercise!!!")
  else:
    print("See if you made a mistake in your typing? Or pleaese be direct in your answer about your assignment type.")

#Extra-Cirricular Activites
ExtraCirricularActivitiesInt = int(input("How many extra-cirriculum actvities do you have today?: "))
for activities in range(0, ExtraCirricularActivitiesInt, 1):
  ExtraCirricularActivityStr = str(input("What are your extra-cirricular activites today?: "))
  ExtraCirricularStartTimeInt = input('Please input the start time for when your Extra Cirricular Activity is going to start in format HHMM: \n ')
  ExtraCirricularEndTimeInt = input("Please input the end time for when your Extra Cirricular Activity is going to end in formation HHMM: \n ")

CurrentTime = dt.datetime.now()
print(CurrentTime.strftime("%H:%M"))

NumberOfPeriodsHomeworkFinished = 0

print("Thank You for this information! Now a schedule will be created for you!")
print("Student Name:" + StudentNameStr + "               " + "Student Grade: " + StudentGradeStr)

for NumberOfHomeworkPeriodsFinished in range(NumberOfPeriodsHomeworkFinished, StudentPeriodsOrClassesInt+1, 1):
  if NumberOfPeriodsHomeworkFinished < StudentPeriodsOrClassesInt:
    print("Continue working on your assignment!")
    print("Start on your assignment for 50 minutes")
    MultipleEncouragementWords()
    print("Now, take a break for ten minutes by walking around for sometime")
    time.sleep(5)#change this
    NumberOfPeriodsHomeworkFinished = NumberOfPeriodsHomeworkFinished + 1
  else:
    if NumberOfPeriodsHomeworkFinished == StudentPeriodsOrClassesInt:
      print("You are finished with your homework!!")
      print("Now try studying for your test and quiz, if you have one. Or else, you are currently free. Try reading a book for fun!")