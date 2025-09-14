course = "PytHon for BeGinners"
another_course2 = (course.replace("BeGinners", "Absolute Beginners"))
print(len(course)) # general purpose function -gives you the number of characters in the string, but can do other things
# course. gives you all the methods that you can apply to stings
print(course.upper())
print(course.lower())
print(course.swapcase())

print(course.find("fo")) #case sensitive
print(course.replace("BeGinners", "Absolute Beginners")) #case sensitive
print(another_course2)
print("PytHon" in course)
print("pytHon" in course) #case sensitive

