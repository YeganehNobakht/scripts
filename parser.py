import os
import json 
import yaml 

def parse_json(file_name):
    with open(file_name, "r") as file:
        file_content = json.load(file)
    return file_content;

def parse_yml(file_name):
    with open(file_name, "r") as file:
        file_content = yaml.safe_load(file)
    return file_content;


def print_yml_file(file_name):
    yml_content = parse_yml(file_name)
    print
    for key , value in yml_content.items():
        print(f"key is: {key}")
        print(f"value is: {value}")


def write_json_to_file(content, dest_file):
    with open(dest_file, "w") as file:
        json.dump(content, file, indent=4)

def convert_yml_to_json(yml_file_name, json_file_name):
    yml_content = parse_yml(yml_file_name)
    write_json_to_file(yml_content, json_file_name)

def write_yml_to_file(content, dest_file):
    with open(dest_file, "w") as file:
        yaml.dump(content, file, indent=4)

def convert_json_to_yml(json_file_name, dest_yml_file):
    yml_content = parse_json(json_file_name)
    write_yml_to_file(yml_content, dest_yml_file)

def toggle_file_type(file_name, converted_file):
    name, ext = os.path.splitext(file_name)
    if ext == ".yml" or ext == ".yaml":
        convert_yml_to_json(file_name, converted_file)
    elif ext == ".json":
        convert_json_to_yml(file_name, converted_file)


def main():
    # print(json_parser("info.json"))
    # print_yml_file("info.yml")
    # convert_yml_to_json("info.yml", "yml_to_json.json")
    # convert_json_to_yml("info.json", "json_to_yml.yml")
    toggle_file_type("info.json", "toggle.yml")





if __name__ == "__main__":
    main()