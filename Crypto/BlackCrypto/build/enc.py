from string import ascii_letters

enc = ''
print('Input key: ')
key = input()
print('Input text: ')
text = input()
count = 0
for i in text:
    if i not in ascii_letters: enc += str(i)
    if count == len(key):count = 0
    enc += str((int(ord(i)) * ord(key[count]) + (ord(key[count])+1))%26)
    count += 1
print(f"Encrypt text: {enc}")