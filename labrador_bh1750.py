import gpiod
from periphery import I2C
import time

class BH1750:
    I2C_BUS = "/dev/i2c-2"
    I2C_ADDR = 0x23
    POWER_ON = 0x01
    MODE_CONTINOUS = 0x10
    MEASURE_COMMAND = [0xAC, 0x23, 0x00]

## Global
i2c = I2C(BH1750.I2C_BUS)

def bh1750_init():
    i2c.transfer(BH1750.I2C_ADDR, [I2C.Message(BH1750.POWER_ON)])
    time.sleep(0.01)

    i2c.transfer(BH1750.I2C_ADDR, [I2C.Message(BH1750.MODE_CONTINOUS)])
    time.sleep(0.12)

    return i2c

def bh1750_read():
    i2c.transfer(BH1750.I2C_ADDR, [I2C.Message(BH1750.MEASURE_COMMAND)])
    time.sleep(0.09)

    read_value = i2c.transferer(BH1750.I2C_ADDR, [I2C.Message([] ,read=True, length=2)])
    data = read_value.data

    lux_raw

    lux = (lux_raw)

    return lux_

def main():
    bh1750_init()

    while True:
        lux = bh1750_read()
        print(f"Valor Luminosidade: {lux:.2f}")
