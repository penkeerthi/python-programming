def encode_string(string):
    letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z']
    
    result = ''
    for character in string:
        for idx in range(len(letters)):
            if character == letters[idx]:
                result += str(idx + 1)
    return result

print(encode_string('happy'))
print(encode_string('abc'))

'''result = ''
for character in string:
    for idx in range (letters):
        if character == letters[idx]:
            result += idx + 1
        idx += 1
'''

