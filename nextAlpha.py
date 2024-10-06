alpha = 'abcdefghijklmnopqrstuvwxyz'
#all the alphabets
s1 = input()
s = s1.lower()
#converts all the alphabets into lower case for the comparison with the alphabets(in alpha)
i = 0
t = '' #empty string where everything is appended to
while (i<len(s)): #the condition is true as long as the ith term is less than the number of characters
    t = t+str(alpha[((alpha.index(s[i])+1)%26)])
    #alpha.index(s[i]) finds the index of the ith element in the alphabet set, then the "+1" makes it move to the next alphabet (one extra index, for example, 18 to 19). "%26" makes sure that a next alphabet of 'z' can be found without an error (i.e. 'a')
    i += 1
    #increments i by 1 (moving to the next ith term)
print(t)