from monster_characteristics import *
from student_monster import *
from course import *

# Create two student objects
mike = Student('mike', 567, 'fluffy blue', 1)
randall = Student('randall', 666, ' lizard shiny purple', 5)

# Add a skill to each of your student
mike.add_skill('super strength')
randall.add_skill('camouflage skin')

# Create(initialize) a course
monster_course = Course('Stealth training','02/06/20')

# Append student object / instances to list of student attributes in one of the courses
monster_course.add_student(mike)
monster_course.add_student(randall)



print(monster_course.get_students())


# Debugging options
  # check the original class
  # look for what get_skills method does
  # look what and skills method does
  # check its type

  # program till we get the results we want
  # be a plumber of code

  # point break
    # Point break stops your code in real time, allowing your variables at that point in time.

# EXTRA - get the list of students, itterate over it and print the students name


