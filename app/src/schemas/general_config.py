from enum import Enum


class LangCode(str, Enum):
    EN = "en"
    VN = "vn"


class ModelCode(str, Enum):
    OPENAI_API = "gpt-3.5-turbo"
