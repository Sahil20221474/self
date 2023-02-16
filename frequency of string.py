string = 'hello world! this is qwerty'

print(string)

freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters in",string, "is :", "\n " + str(freq))
