import os
from datetime import datetime

class MicroSD:
    
    def __init__(self, storage_path='dados_sd'):

        self.storage_path = storage_path
        
        try:
            os.makedirs(self.storage_path, exist_ok=True)
            print(f"Diretório de armazenamento '{self.storage_path}' está pronto.")
        except OSError as e:
            print(f"Erro ao criar o diretório '{self.storage_path}': {e}")

            raise

    def write(self, filename, content):

        full_path = os.path.join(self.storage_path, filename)
        
        try:
            with open(full_path, 'w') as f:
                f.write(content)
            print(f"Arquivo '{filename}' salvo com sucesso em '{self.storage_path}'.")
            return True
        except IOError as e:
            print(f"Erro de E/S ao tentar escrever o arquivo '{filename}': {e}")
            return False
        except Exception as e:
            print(f"Um erro inesperado ocorreu ao escrever o arquivo: {e}")
            return False

    def append(self, filename, content):

        full_path = os.path.join(self.storage_path, filename)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {content}\n"
        
        try:
            with open(full_path, 'a') as f:
                f.write(log_entry)
            return True
        except IOError:
            return False

    def delete(self, filename):
        
        full_path = os.path.join(self.storage_path, filename)
        
        try:
            if os.path.exists(full_path):
                os.remove(full_path)
                print(f"Arquivo '{filename}' deletado com sucesso.")
                return True
            else:
                print(f"Erro: O arquivo '{filename}' não foi encontrado para deleção.")
                return False
        except OSError as e:
            print(f"Erro ao deletar o arquivo '{filename}': {e}")
            return False
            
    def list_files(self):
        
        try:
            files = os.listdir(self.storage_path)
            print(f"Arquivos em '{self.storage_path}': {files}")
            return files
        except OSError as e:
            print(f"Erro ao listar arquivos em '{self.storage_path}': {e}")
            return []
