temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]
positive_count = 0
negative_count = 0

for readings in temperature_readings:
    if readings > 0:
        positive_count += readings
    else:
        negative_count += readings

print ('Average of Positive Count:',positive_count)
print ('Average of Negative Count:',negative_count)
         

