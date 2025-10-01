# Labrador: Sensor de Luminosidade Inteligente

Este projeto transforma sua placa Labrador em um dispositivo inteligente e reativo à luz ambiente.

Utilizando um sensor de luminosidade BH1750, este código lê a intensidade da luz, controla os LEDs internos da placa com base em um limite pré-definido e, o mais importante, **cria um log contínuo de dados** salvando todas as leituras em um cartão MicroSD.

É a base perfeita para projetos de automação, monitoramento ambiental ou simplesmente para aprender a integrar hardware com Python de forma organizada e modular.

## ✨ Funcionalidades

* **Leitura de Luminosidade:** Interface com o sensor I2C BH1750 para obter medições precisas em Lux.
* **Controle de LEDs:** Aciona os LEDs internos da placa quando a luminosidade cai abaixo de um limite configurável, funcionando como uma luz noturna automática.
* **Log de Dados:** Salva cada leitura do sensor, com data e hora, em um arquivo de log no cartão MicroSD, ideal para análises futuras.
* **Código Modular:** O projeto é organizado em classes Python, separando as responsabilidades do sensor, do cartão SD e dos LEDs, facilitando a manutenção e a reutilização do código.

## 🚀 Como Usar

### Hardware Necessário
1.  Placa Labrador
2.  Sensor de Luminosidade BH1750
3.  Cartão MicroSD formatado
4.  Jumpers para a conexão

### Configuração
1.  **Conexão Física:** Conecte o sensor BH1750 aos pinos I2C corretos da sua placa Labrador (consulte o pinout da placa para os barramentos `/dev/i2c-0`, `/dev/i2c-2`, etc.).
2.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/Labrador_BH1750.git](https://github.com/seu-usuario/Labrador_BH1750.git)
    cd Labrador_BH1750
    ```
3.  **Ajuste as Configurações:** Abra o arquivo `main.py` e ajuste as constantes no topo do arquivo:
    * `LUMINOSITY_THRESHOLD`: O valor em Lux que define quando os LEDs devem acender.
    * `LED_NAMES`: Os nomes exatos dos LEDs da sua placa (encontre-os com `ls /sys/class/leds/`).
    * `storage_path`: O caminho exato para o ponto de montagem do seu cartão MicroSD (ex: `'/media/caninos/EXTERNO'`).

### Execução
Como o script precisa de acesso ao hardware (I2C e LEDs), ele deve ser executado com permissões de administrador:
```bash
sudo python3 main.py
```

Pronto! O terminal começará a exibir as leituras de luminosidade, e os dados serão salvos no seu cartão SD enquanto os LEDs reagem à luz ambiente.

## 📁 Estrutura do Projeto

```
/
├── main.py               # Script principal que integra tudo
├── sensor/
│   ├── bh1750.py         # Classe para o sensor de luz
│   ├── microSD.py        # Classe para gerenciar o SD Card
│   └── internal_leds.py  # Classe para controlar os LEDs
└── README.md             # Este arquivo
```

Sinta-se à vontade para explorar, modificar e usar este projeto como base para suas próprias criações!
