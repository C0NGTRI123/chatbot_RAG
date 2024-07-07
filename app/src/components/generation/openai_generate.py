import openai
from .base import BaseGenerator
import decouple
from dotenv import load_dotenv

# Set API Key
# load_dotenv()
# openai.api_key = decouple.config("OPENAI_API_KEY")


class OpenAIGenerator(BaseGenerator):
    def __init__(self,
                 prompt: str,
                 model_name: str = "gpt-3.5-turbo",
                 system_message: str = "You are a helpful assistant.",
                 temperature: float = 0,
                 json_mode: bool = False,
                 **kwargs
                 ):
        self.prompt = prompt
        self.model_name = model_name
        self.system_message = system_message
        self.temperature = temperature
        self.json_mode = json_mode

    def generate(self):
        if self.json_mode:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                temperature=self.temperature,
                top_p=1,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": self.prompt},
                ],
            )
            return response.choices[0].message.content
        else:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                temperature=self.temperature,
                top_p=1,
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": self.prompt},
                ],
            )
            return response.choices[0].message.content
