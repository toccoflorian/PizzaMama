
import json

class StorageManager:

    def load_data(self, data_name):
        filename = self.get_filename(data_name)
        try:
            file = open(filename, "r")
            data = file.read()
        except:
            return ""
        return json.loads(data)

    def save_data(self, data_name, data_content):
        filename = self.get_filename(data_name)
        file = open(filename, "w")
        data_json = json.dumps(data_content)
        file.write(data_json)

    def get_filename(self, data_name):
        return data_name + ".json"
