course = "Python's course for Beginners" # double quotes mean you can use '
course2 = 'Python for "beginners"' # signle quotes around the string mean you can "" arounn beginners
course3 = '''
Hi David 

Here is our first email to you

Thank you 

team amzeballs


'''
another_course = course[:]
print(course)
print(course2)
print(course3)
print(course[0]) #[] returns the first letter of the index
print(course[-1]) #[-1] returns the last letter of the index i.e. counts backwards
print(course[0:6]) # returns a series of indexes it excludes the last number
print(course[10:]) # blank after : runs to the end on the string
print(course[:10]) # blank before : runs from start on the string
print(another_course)
print(course[0:-0])
