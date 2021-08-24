#help('print')
total_distance_in_km=10
total_distance_in_m=total_distance_in_km*0.621371
time_seconds=30
time_minutes=43+(time_seconds/60)
time_hours=time_minutes/60
avg_speed=total_distance_in_m/time_hours
avg_speed=str(round(avg_speed,2))
print('The average speed in miles per hour is',avg_speed)

