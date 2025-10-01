import os

class InternalLEDs:
    BASE_PATH = "/sys/class/leds/"

    def __init__(self, led_names):
        self.led_names = led_names
        print(f"Assumindo controle dos LEDs: {self.led_names}")
        
        for name in self.led_names:
            trigger_command = f"sudo sh -c 'echo none > {self.BASE_PATH}{name}/trigger'"
            os.system(trigger_command)

    def _set_brightness(self, value):
        if value not in [0, 1]:
            return

        for name in self.led_names:
            brightness_command = f"sudo sh -c 'echo {value} > {self.BASE_PATH}{name}/brightness'"
            os.system(brightness_command)

    def turn_on(self):
        print("LEDs LIGADOS")
        self._set_brightness(1)

    def turn_off(self):
        print("LEDs DESLIGADOS")
        self._set_brightness(0)
