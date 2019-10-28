#worker_type = 'full_time' or 'part_time' or 'contract'
worker_type = 'contract'
full_timepay = 50
part_timepay = 65
contract_pay = 120 - ((120*25)/100)
hour = 40
fulltime_weekly_wage = 0
parttime_weekly_wage = 0
contract_weekly_wage = 0
#for worker_type in worker_type:
if worker_type == 'full_time': #and worker_type != 'part_time' :
    #full_timepay * hour = fulltime_weekly_wage
    fulltime_weekly_wage = full_timepay * hour
    print(f'Full time workers Weekly wage= {fulltime_weekly_wage}')
elif worker_type == 'part_time': #and worker_type != 'contract':
    parttime_weekly_wage = part_timepay * hour
    print(f'Part time workers Weekly wage= {parttime_weekly_wage}')
else worker_type == 'contract':
    contract_weekly_wage = contract_pay * hour
    print(f'Contract workers Weekly wage= {contract_weekly_wage}')

