from monster_characteristics import *
from student_monster import *
from course import *

# Create two student objects
Mike = Student('Mike', 567,'fluffy blue',1)
Randall = Student('Randall',666,' lizard shiny purple',5)

# Add a skill to each of your student
Mike.add_skill('super strength')
Randall.add_skill('camouflage skin')

# Create(initialize) a course
monster_course = Course('Stealth training','02/06/20')

# Append student object / instances to list of student attributes in one of the courses
monster_course.add_student(Mike)
monster_course.add_student(Randall)

monster_course.add_skill()
print(monster_course.skill_list)


# EXTRA - get the list of students, itterate over it and print the students name