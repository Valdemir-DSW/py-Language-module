#Language file reader (.vidm) By Valdemir

'''
................................................
................................................
................................................
................................................
................................................
................................................
................................................
................................................
................................................

................................................

................................................

................................................

................................................


................................................
'''
import os
import pickle
import random
import json
import platform

class idmManager:
    def __init__(self, file_path, save_in_appdata=False):
        self.file_path = file_path
       
        if save_in_appdata:
            self.app_data_path = self._get_app_data_path()
        else:
            self.app_data_path = None
    
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"O arquivo de idiomas '{self.file_path}' não foi encontrado.")
       
        with open(self.file_path, "rb") as file:
            self.data = pickle.load(file)
        self.current_language = self._load_last_language()

    def _get_app_data_path(self):
        """Detecta automaticamente o caminho do AppData dependendo do sistema operacional."""
        system = platform.system()
        if system == "Windows":
            app_data = os.getenv('APPDATA')  # Caminho padrão no Windows
            return os.path.join(app_data, "meu_app", "app_data.json")
        elif system == "Linux" or system == "Darwin":  # Darwin é o nome do macOS no Python
            home_dir = os.path.expanduser("~")
            return os.path.join(home_dir, ".config", "meu_app", "app_data.json")
        else:
            raise EnvironmentError(f"Sistema operacional '{system}' não suportado para salvar dados de idioma.")

    def _load_last_language(self):
        """Carrega o último idioma selecionado do arquivo de dados do aplicativo."""
        if self.app_data_path and os.path.exists(self.app_data_path):
            try:
                os.makedirs(os.path.dirname(self.app_data_path), exist_ok=True) 
                with open(self.app_data_path, "r") as file:
                    data = json.load(file)
                    last_language = data.get("last_language")
                    if last_language and last_language in self.data:
                        return last_language
                    else:
                        print(f"Idioma salvo não encontrado ou inválido. Usando idioma padrão.")
            except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
                print(f"Erro ao carregar o idioma salvo: {e}")
        return random.choice(list(self.data.keys()))

    def _save_last_language(self):
        """Salva o idioma atual no arquivo de dados do aplicativo."""
        if self.app_data_path:
            try:
                os.makedirs(os.path.dirname(self.app_data_path), exist_ok=True)  # Cria o diretório se não existir
                with open(self.app_data_path, "w") as file:
                    json.dump({"last_language": self.current_language}, file)
            except Exception as e:
                print(f"Erro ao salvar o idioma atual: {e}")

    def set_language(self, language):
        """Muda o idioma para o especificado e salva essa escolha."""
        if language in self.data:
            self.current_language = language
        else:
            random_lang = random.choice(list(self.data.keys()))
            print(f"Aviso: Idioma '{language}' não disponível. Usando '{random_lang}' como padrão.")
            self.current_language = random_lang
        
        self._save_last_language()

    def get_content(self, id_key):
        """Obtém o conteúdo do idioma atual baseado no id_key."""
        if self.current_language:
            try:
                return self.data[self.current_language].get(id_key, f"ID '{id_key}' não encontrado no idioma '{self.current_language}'.")
            except KeyError:
                return f"Erro: ID '{id_key}' não encontrado no idioma '{self.current_language}'."
        else:
            return "Erro: Nenhum idioma definido. Use a função 'set_language' para selecionar o idioma."
