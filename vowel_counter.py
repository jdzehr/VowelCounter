string1 = input("Enter a string: ")
print(string1)
string1 = string1.lower()
vowels = ('a','e','i','o','u')

# vowelNumbers = [Total, A's, E's, I's, O's, U's]
vowelNumbers = [0,0,0,0,0,0]

for j in range(0, len(string1)):
    for k in range(0, len(vowels)):
        if string1[j] == vowels[k]:
            vowelNumbers[k+1] += 1
            vowelNumbers[0] += 1

print("Total Vowels = %s\nTotal A counts = %s\nTotal E counts = %s\nTotal I counts = %s\nTotal O counts = %s\nTotal U counts = %s\n" % (str(vowelNumbers[0]),str(vowelNumbers[1]),str(vowelNumbers[2]),str(vowelNumbers[3]),str(vowelNumbers[4]),str(vowelNumbers[5]))) 