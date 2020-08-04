# 1 numbers
print('numbers:\n')

num=[0,6, 35, 1, 77, 85, 63, 39, 71, 39, 98, 19]
print('Original appearance: '+str(num))

a = num.index(min(num))
b = num.index(max(num))
num[a], num[b] = num[b], num[a]

print('index min: '+str(a)+'\n'+'index max: '+str(b))
print('Altered: '+str(num))

# 2 alphabet
print('\nAlphabet:\n')

alphabet=['t', 'a', 'b', 'h', 'i', 'u', 'z']
print('Original appearance: '+str(alphabet))

a = alphabet.index(min(alphabet))
b = alphabet.index(max(alphabet))
alphabet[a], alphabet[b] = alphabet[b], alphabet[a]

print('index min: '+str(a)+'\n'+'index max: '+str(b))
print('Altered: '+str(alphabet))