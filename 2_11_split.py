sentence = input("\n Enter the sentence\t: ")
print("\n Original String\t: ",sentence[:])

string = sentence.split()
string1 = ' '.join(reversed(string))

print("\n Reverse string : ",string1.split())