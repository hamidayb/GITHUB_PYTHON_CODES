s = input("Enter a string: ")
sub = input("Enter a substring: ")
c = 0
for i in range(len(s)):
    if(s.find(sub,i,i+len(sub)) != -1):
        c+=1

print(c)
