s1 = 'dead'
s2 = 'beef'
s3 = 'beadfeed'
chars = []

for char in s1:
    chars.append(char)
    
for char in s2:
    chars.append(char)
    
chars.sort()

third_string = []
for char in s3:
    third_string.append(char)
    
third_string.sort()

if chars == third_string:
    print "True!"