import json
import re
import time

from app.src.utils.pydantic import PydanticOutputParser
# from app.src.utils.translation_agent import translate
from app.src.schemas.general_config import LangCode, ModelCode
from tqdm import tqdm

PATTERN_LST = [r'```json\n(.*)\n```', r'```\n(.*)\n```']


def post_process_res(text: str, document_type: str):
    # Extract JSON string from the text
    try:
        data = eval(text)
    except:
        match = re.search(PATTERN_LST[0], text, re.DOTALL) or re.search(PATTERN_LST[1], text, re.DOTALL)
        if match is None:
            raise ValueError("No JSON string found in the text")
        try:
            data = json.loads(re.sub("//.*", "", match.group(1), flags=re.MULTILINE))
        except:
            data = eval(re.sub("//.*", "", match.group(1), flags=re.MULTILINE))
    return DOC_TYPE_INFO.get(document_type)(**data)


class KieService(object):
    def extract(
        self,
        text,
        document_type,
        lang,
        model_name: str = ModelCode.OPENAI_API,
    ) -> str:
        if document_type not in DOC_TYPE_INFO:
            raise ValueError(f"Not support with document {document_type.value}")
        pydantic_parser = PydanticOutputParser(pydantic_object=DOC_TYPE_INFO.get(document_type.value))
        format_instructions = pydantic_parser.get_format_instructions()
        few_shot_examples = DOC_TYPE_PROMPT.get(document_type.value).get(lang.value)
        # f"{few_shot_examples}\n" \
        # prompt = f"Your current task is to extract information. \n" \
        #          f"Context information is below:\n" \
        #          f"---------------------------------------------------\n" \
        #          f"---------------------------------------------------\n" \
        #          f"Given the context information and not prior knowledge, answer the query: \n" \
        #          f"Query: \n{text}\n" \
        #          f"Answer: \n{format_instructions}"
        prompt = f"Return the list of articles/items/services with their completed information about 3 fields: 'description', 'quantity' and 'ttc amount' if available, in json format. The table is: \n{text}"
        start_time = time.time()
        response = LLMGenerator(prompt, model_name).generate()
        print(f"Time to process: {time.time() - start_time}")
        # data = post_process_res(response, document_type=document_type)
        # return data
        return response


if __name__ == "__main__":
    import os

    a = KieService()
    folder_path = "/home/rb074/Downloads/plot/prompt_2"
    list_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    # Translate text
    # source_lang, target_lang, country = "French", "English", "English"

    for file in tqdm(list_files[:]):
        with open(os.path.join(folder_path, file), "r") as f:
            text4prompt = f.read()
            # text4prompt = translate(
            #     source_lang=source_lang,
            #     target_lang=target_lang,
            #     source_text=text4prompt,
            #     country=country,
            # )

            # with open(os.path.join(folder_path, file.replace(".txt", "_translated.txt")), "w") as f:
            #     f.write(text4prompt)

            text = a.extract(text4prompt, DocTypeCode.RECEIPT, LangCode.FR, ModelCode.LLAMA3_8B_F16)
            with open(os.path.join(folder_path, file.replace(".txt", "_response.txt")), "w") as f:
                f.write(text)
                # f.write(text)
