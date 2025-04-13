import json
import yaml
from pathlib import Path
import os

class ConfigurationManager:
    def __init__(self, file_path=None):
        self.config = {}
        if file_path:
            self.file = self.load(file_path)

    def load(self, file_path):
        file_path = Path(file_path)
        if file_path.suffix == ".json":
            with open(file_path, "r") as f:
                self.config = json.load(f)
        elif file_path.suffix in [".yaml", ".yml"]:
            print(os.getcwd())
            with open(file_path, "r") as f:
                self.config = yaml.safe_load(f)
        else:
            raise ValueError("Unsupported file format. Use .json or .yaml/.yml")
        
    def save(self, file_path):
        file_path = Path(file_path)
        if file_path.suffix == ".json":
            with open(file_path, "w") as f:
                json.dump(self.config, f, indent=4)
        elif file_path.suffix in [".yaml", ".yml"]:
            with open(file_path, "w") as f:
                yaml.safe_dump(self.config, f, sort_keys=False)
        else:
            raise ValueError("Unsupported file format. Use .json or .yaml/.yml")
    
    def add_config(self, key, value):
        self.config[key] = value

    def update_config(self, key, value):
        if key in self.config:
            self.config[key] = value
        else:
             print(f"Key '{key}' does not exist. Use add_config to add new keys.")

    def get_config(self, key):
        # Returns None if the key does not exist.
        return self.config.get(key)
    


# Example usage:
if __name__ == "__main__":

    config_mgr = ConfigurationManager("./configuration-manager/config.yml")  # Load from a sample YAML file
    
    config_mgr.add_config("username", "admin")
 
    config_mgr.update_config("debug", False)

    print(f"App Name: {config_mgr.get_config('app_name')}")

    config_mgr.save("./configuration-manager/updated_config.yml")
        