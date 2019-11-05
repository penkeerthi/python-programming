temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]

positive_sum = 0
negative_sum = 0
positive_count = 0
negative_count = 0

for reading in temperature_readings:
    if reading > 0:
        positive_sum += reading
        positive_count += 1
    else:
        negative_sum += reading
        negative_count += 1

print('Average of positive reading {}'.format(positive_sum / positive_count))
print('Average of negative reading {}'.format(negative_sum / negative_count))
