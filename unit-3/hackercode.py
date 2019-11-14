def filter_list(l):
    a_list = [] #Defining a list
    for item in l: #searching for an iterable item in list i
        if type(item) is not str:
            a_list.append(item)
    return a_list
  #'return a new list with the strings filtered out'


'''
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

'''

'''

def filter_list(l):
    for value in l:
        if type(value) is  str:
        l.remove(value) #dangerours - never want to change lists while iteratin
    return l

print(filter_list([1,2,'a','b',5]))

'''