from string import ascii_lowercase as alphabet

for i in alphabet:
    print(i)

iterator = iter(alphabet)
next_letter = next(iterator)

print(next_letter)
