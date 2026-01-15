time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minut = 0
time_values = time_values.replace(' ', ',')
time_values = time_values.split(',')
for time in time_values:
    if 'h' in time:
        time = int(time.replace('h', ''))
        total_minut += 60*time
    elif 'm' in time:
        time = int(time.replace('m', ''))
        total_minut += time
    elif 's' in time:
        time = int(time.replace('s', ''))
        total_minut += time//60
print(total_minut)