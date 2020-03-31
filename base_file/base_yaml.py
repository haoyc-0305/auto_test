import yaml
from base_file.base_file_route import yaml_path


def data_yaml(file_name):
    with open(yaml_path() + file_name + ".yaml", "rb") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
