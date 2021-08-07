#wap to read a string and count the number of vowels,
# and count the number of consonents.

s1 = input("Enter a string: ")
vc, cc = 0, 0

for s in s1:                         #for every character in the string
              if s.isalpha():
                         if s in "AEIOUaeiou"  :
                                        vc += 1

                         else:
                                        cc += 1
print(vc, cc)
                           

