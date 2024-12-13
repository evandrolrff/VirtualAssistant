import json
import os

class LanguageManager:
    def __init__(self, language_directory="messages", default_language="en") -> None:
        """
        Gerencia as mensagens de diferentes idiomas armazenadas em arquivos JSON.
        :param language_directory: Diretório onde os arquivos de idioma estão localizados.
        :param default_language: Idioma padrão.
        """
        self.language_directory = language_directory
        self.current_language = default_language
        self.messages = {}
        self.load_language(default_language)


    def load_language(self, language_code) -> None:
        """
        Carrega mensagens de um arquivo JSON baseado no código de idioma.
        :param language_code: Código do idioma (ex.: 'en', 'pt').
        """
        # Join o diretório e o código de idioma para criar o subcaminho
        language_subpath = os.path.join(self.language_directory, language_code)

        # Baseando-se no diretório do arquivo atual
        language_file = os.path.join(os.path.dirname(__file__), f"{language_subpath}.json")
        if os.path.exists(language_file):
            with open(language_file, "r", encoding="utf-8") as file:
                self.messages = json.load(file)
            self.current_language = language_code
        else:
            raise FileNotFoundError(f"Language file '{language_file}' not found.")


    def set_language(self, language_code) -> None:
        """
        Define o idioma atual da aplicação.
        :param language_code: Código do idioma (ex.: 'en', 'pt').
        """
        self.load_language(language_code)

    
    def get_message(self, key):
        """
        Retorna a mensagem correspondente ao idioma atual.
        :param key: Chave da mensagem.
        :return: Mensagem traduzida.
        """
        return self.messages.get(key, "Message not found.")