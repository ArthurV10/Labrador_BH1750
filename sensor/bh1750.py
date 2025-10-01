from periphery import I2C
import time

class BH1750:
    I2C_BUS = "/dev/i2c-2"
    I2C_ADDR = 0x23
    POWER_ON = 0x01
    MODE_CONTINUOUS_HIGH_RES = 0x10

    def __init__(self, bus=I2C_BUS, addr=I2C_ADDR):
        self.i2c = I2C(bus)
        self.addr = addr
        
        self._init_sensor()

    def _init_sensor(self):
        self.i2c.transfer(self.addr, [I2C.Message([self.POWER_ON])])
        time.sleep(0.01)

        self.i2c.transfer(self.addr, [I2C.Message([self.MODE_CONTINUOUS_HIGH_RES])])
        time.sleep(0.12)

    def read(self):
        read_msg = [I2C.Message([0x00] * 2, read=True)]
        self.i2c.transfer(self.addr, read_msg)

        data = read_msg[0].data
        lux_raw = (data[0] << 8) | data[1]
        lux = lux_raw / 1.2

        return lux
        
    def close(self):
        self.i2c.close()