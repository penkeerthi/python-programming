def list_to_dict(people):
    result = {}
    for item in people:
        result[item[0]] = item[1]

    return result

person = {['name','alice'], ['job','Engineer'],['city','toronto']}

'''

def frequency_counter(string):
    result = {}
    for character in string:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    
    return result
#print(frequency_counter('happy'))
def list_to_dict(people):
    result = {}
    for item in people:
        result[item[0]] = item[1]
    
    return result
person = [['name', 'Alice'], ['job', 'Engineer'], ['city', 'Toronto']]
print(list_to_dict(person))
'''