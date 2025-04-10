from json import load, dumps
from yaml import dump, safe_load

def json_parser(file_name):
    with open(file_name, "r") as file:
        file_content = load(file)
    return file_content;

def yaml_parser(file_name):
    with open(file_name, "r") as file:
        file_content = safe_load(file)
    return file_content;


def print_yml_file(file_name):
    yml_content = yaml_parser(file_name)
    print
    for key , value in yml_content.items():
        print(f"key is: {key}")
        print(f"value is: {value}")

def main():
    # print(json_parser("info.json"))
    print_yml_file("info.yml")




if __name__ == "__main__":
    main()