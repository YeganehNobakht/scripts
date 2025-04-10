import json 
import yaml 

def json_parser(file_name):
    with open(file_name, "r") as file:
        file_content = json.load(file)
    return file_content;

def yaml_parser(file_name):
    with open(file_name, "r") as file:
        file_content = yaml.safe_load(file)
    return file_content;


def print_yml_file(file_name):
    yml_content = yaml_parser(file_name)
    print
    for key , value in yml_content.items():
        print(f"key is: {key}")
        print(f"value is: {value}")


def write_json_to_file(content, dest_file):
    with open(dest_file, "w") as file:
        json.dump(content, file, indent=4)

def convert_yml_to_json(yml_file_name, json_file_name):
    yml_content = yaml_parser(yml_file_name)
    write_json_to_file(yml_content, json_file_name)

def main():
    # print(json_parser("info.json"))
    # print_yml_file("info.yml")
    convert_yml_to_json("info.yml", "yml_to_json.json")





if __name__ == "__main__":
    main()