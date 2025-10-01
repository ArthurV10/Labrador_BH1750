from sensor.bh1750 import BH1750
from sensor.microSD import MicroSD
import time

def main():
    print("Iniciando sensor BH1750...")

    bh1750 = BH1750()
    # Coloque o caminho do seu SD_CARD
    sdCard = MicroSD(storage_path='/media/caninos/EXTERNO')

    print("Sensor pronto. Pressione Ctrl+C para sair.")

    try:
        while True:
            lux = bh1750.read()
            data_to_write = f"Valor Luminosidade: {lux} Lux"
            if (sdCard.append("logs_lux.txt", data_to_write)):
                print("Valor Salvo!")
            else:
                print("ERRO: Falha ao salvar no SD Card.")

            print(f"Valor luminosidade: {lux:.2f} Lux")

            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nPrograma Encerrado.")
    finally:
        bh1750.close()

if __name__ == "__main__":
    main()