# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

print("initializing sensor")
print("wait 15 seconds")

import uSGP30
import machine
import time


I2C_SCL_GPIO = const(22)
I2C_SDA_GPIO = const(21)
I2C_FREQ = const(4000)
i2c = machine.I2C(-1,
    scl=machine.Pin(I2C_SCL_GPIO, machine.Pin.OUT),
    sda=machine.Pin(I2C_SDA_GPIO, machine.Pin.OUT),
    freq=I2C_FREQ
)


print(i2c.scan())
sgp30 = uSGP30.SGP30(i2c)

time_stupid = 0

while True:
    co2eq_ppm, tvoc_ppb = sgp30.measure_iaq()
    print(co2eq_ppm, tvoc_ppb)
    
    csv=open("data.csv","at")
    csv.write(f"{time_stupid},{co2eq_ppm},{tvoc_ppb}\n")
    csv.close()
    
    time_stupid += 10
    
    time.sleep(10)
