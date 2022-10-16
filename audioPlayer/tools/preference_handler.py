import json
import logging

class PreferenceFileHandler():
    path = "../preferences.json"

    @classmethod
    def get_base_directory(cls):
        with open(cls.path, "r") as preferences:
            data = json.load(preferences)
            return data["baseDir"]

    @classmethod
    def set_base_directory(cls, new_base_dir):
        data = None
        with open(cls.path, "r") as preferences:
            data = json.load(preferences)
            preferences.close()
        with open(cls.path, "w") as preferences:
            data["baseDir"] = new_base_dir
            json.dump(data, preferences)
        logging.info(f"New base directory set at {data}")

