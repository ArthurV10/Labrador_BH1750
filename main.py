from sensor.bh1750 import BH1750
from sensor.microSD import MicroSD
from sensor.internal_leds import InternalLEDs
import time

def main():
    LUMINOSITY_THRESHOLD = 29
    LED_NAMES = ['led1', 'led2']

    print("Iniciando sensor BH1750...")

    bh1750 = BH1750()
    # Coloque o caminho do seu SD_CARD
    sdCard = MicroSD(storage_path='/media/caninos/EXTERNO')
    leds = InternalLEDs(led_names=LED_NAMES)

    print("Sensor pronto. Pressione Ctrl+C para sair.")

    try:
        while True:
            lux = bh1750.read()
            log_data = f"Valor Luminosidade: {lux} Lux"
            if (sdCard.append("logs_lux.txt", log_data)):
                print("Valor Salvo!")
            else:
                print("ERRO: Falha ao salvar no SD Card.")
            
            if lux > LUMINOSITY_THRESHOLD:
                leds.turn_on()
            else:
                leds.turn_off()

            print(f"Valor luminosidade: {lux:.2f} Lux")

            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nPrograma Encerrado.")
    finally:
        leds.turn_off()
        bh1750.close()

if __name__ == "__main__":
    main()