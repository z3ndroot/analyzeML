import json


class JSONMetaData:
    def __init__(self, filename: str):
        self.filename = filename
        self.meta_info = self.get_meta_info()

    def get_meta_info(self):
        meta_info = []
        with open(self.filename, "r", encoding="UTF8") as file:
            for line in file:
                if not line.replace("\n", ""):
                    continue
                data = json.loads(line)
                meta_info.append(data)
        return meta_info
