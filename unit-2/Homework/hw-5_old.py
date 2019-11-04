temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]

#positive_values = temperature_readings [0]
##positive_values = 0
positive_averages = [] 
'''
for positive_number in temperature_readings:    
           
    if type (positive_number) > 0:
        #positive_number += positive_number
        positive_number.append(positive_values)

        print (positive_number)
'''
#attempt 2
'''
for positive_number in temperature_readings:
    positive_values = 0
    for  positive in positive_number:
        if positive_number >0 :
            positive += positive_number
        print (positive)
'''
#attempt 3
'''
for positive_numbers in temperature_readings:
    if positive_numbers >0:
        positive_averages+=positive_numbers
print(positive_averages)
'''
for positive_number in temperature_readings:
    positive_total = 0
    for number in positive_number:
        positive_total += number
        positive_averages.append(number/len(number))
print (positive_total)
