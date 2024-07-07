from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: str, model_name: str, system_message: str, temperature: float, json_mode: bool):
        """
        Generate a completion based on the given prompt and model.

        Args:
            prompt (str): The user's prompt or query.
            model_name (str): The name of the model to use for generating the completion.
            system_message (str, optional): The system message to set the context for the assistant. Defaults to "You are a helpful assistant.".
            temperature (float, optional): The sampling temperature for controlling the randomness of the generated text. Defaults to 0.5.
            json_mode (bool, optional): Whether to return the response in JSON format. Defaults to False.

        Returns:
            Union[str, dict]: The generated completion. If json_mode is True, returns the complete API response as a dictionary. If json_mode is False, returns the generated text as a string.
        """
        pass
