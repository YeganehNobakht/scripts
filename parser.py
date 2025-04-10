from json import load, dumps
from yaml import dump, safe_load

def json_parser(file_name):
    with open(file_name, "r") as file:
        file_content = load(file)
    return file_content;

def yaml_parser(file_name):
    with open(file_name, "r") as file:
        file_content = safe_load(file)
    return dump(file_content);


def main():
    # print(json_parser("info.json"))
    print(yaml_parser("info.yml"))



if __name__ == "__main__":
    main()