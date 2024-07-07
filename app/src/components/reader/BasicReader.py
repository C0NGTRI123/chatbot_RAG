from wasabi import msg

try:
    from pypdf import PdfReader
except Exception:
    msg.warn("pypdf not installed, your base installation might be corrupted.")

try:
    import docx
except Exception:
    msg.warn("python-docx not installed, your base installation might be corrupted.")


class BasicReader:
    """
    The BasicReader reads .txt, .md, .mdx, .json, .pdf and .docx files.
    """

    def __init__(self, fileData):
        self.fileData = fileData

    def load(self):
        text = []

        for file in self.fileData:
            if file.endswith(".txt") or file.endswith(".md") or file.endswith(".mdx"):
                with open(file, "r"):
                    original_text = file.read()
                text.append(original_text)
            elif file.endswith(".pdf"):
                reader = PdfReader(file)
                full_text = ""
                for page in reader.pages:
                    full_text += page.extract_text() + "\n\n"
                text.append(full_text)
            elif file.endswith(".docx"):
                reader = docx.Document(file)
                full_text = ""
                for paragraph in reader.paragraphs:
                    full_text += paragraph.text + "\n"
                text.append(full_text)
            else:
                msg.warn(f"{file} with extension {file.split('.')[-1]} not supported by BasicReader.")
        return " ".join(text)
