import yagmail
import schedule
import time

yag=yagmail.SMTP('blessingsmapalo541@gmail.com', 'bizf glvc gddu unft')
water_tank = 0
def check_water_tank() : 
    global water_tank
    water_tank = water_tank + 10 - 7
    print(f'Current water level: {water_tank}% - Pump is running.')

with open('tank_log.txt' , 'a') as file : 
     file.write(f'Water level: {water_tank} litres\n')

if water_tank >= 100:
        yag.send('mchanda509@gmail.com', 'WARNING!', 'Water tank is full — pump OFF')
        
        with open('tank_log.txt', 'a') as file:
            file.write('Tank is FULL — pump OFF\n')
        schedule.cancel_job(job)
elif water_tank < 10:
        yag.send('mchanda509@gmail.com', 'WARNING!', 'Low water level — pump ON')


job = schedule.every(10).seconds.do(check_water_tank)

while True:
    schedule.run_pending()
    time.sleep(1)
