paragraph = '''this is testing 
               paragraph for 
               testing three quotes'''
print(paragraph)

String1 = "Educative"

print(String1[3:5])
print(String1[3:-3])

 
String2 = String1 + ' Learner'
print(String2)
 
String3 = String2[:9] + '-' + String2[10:]
print(String3)

string1="Educative"

for a in range(0, len(string1)):
    print(string1[-(a+1)])