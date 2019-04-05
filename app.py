course = 'phyton for me '
print(len(course))
print(course.find('p'))
print(course.upper())
print('me' in course)
print(course.replace('me', 'you'))
course = course.replace('me', 'you')
print('me' in course)

name = input('name')
if len(name)>10:
    print('correct your name')
    name = ''

else:
    print(name)
print(name)