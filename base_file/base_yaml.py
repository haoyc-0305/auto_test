import yaml

file_route = "C:\\Program Files\\JetBrains\\cloud_test\\data_yaml\\"


def data_yaml(file_name):
    with open(file_route + file_name + ".yaml", "rb") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
