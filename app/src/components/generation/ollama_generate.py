import ollama
from .base import BaseGenerator


class OllamaGenerator(BaseGenerator):
    def __init__(self,
                 prompt: str,
                 model_name: str = "ollama3-8b",
                 system_message: str = "You are a helpful assistant.",
                 temperature: float = 0,
                 json_mode: bool = False
                 ):
        self.prompt = prompt
        self.model_name = model_name
        self.system_message = system_message
        self.temperature = temperature
        self.json_mode = json_mode

    def generate(self):
        if self.json_mode:
            responses = ollama.chat(model=self.model_name,
                                    messages=[
                                        {"role": "system", "content": self.system_message},
                                        {"role": "user", "content": self.prompt},
                                    ],
                                    options={"temperature": self.temperature,
                                             "format": "json"})
            return responses['message']['content']
        else:
            responses = ollama.chat(model=self.model_name,
                                    messages=[
                                        {"role": "system", "content": self.system_message},
                                        {"role": "user", "content": self.prompt},
                                    ],
                                    options={"temperature": self.temperature})
            return responses['message']['content']
