# 图片保存路径
def image_path():
    path = "E:\\Python\\cloud_test\\image_file\\"
    return path

# YAML文件路径
def yaml_path():
    path = "E:\\Python\\cloud_test\\data_yaml\\"
    return path

# 文件下载路径
def download_path():
    path = "C:\\Users\\lenovo\\Downloads\\"
    return path

# 上传模版路径
def upload_path():
    path = "C:\\Users\\lenovo\\Downloads\\Chrome_down\\"
    return path

# 数据库连接信息
def database():
    tns = {"oracle": "cloud/cloud@10.1.1.37:1521/cloud",
           "mysql": ["10.1.1.36", "3306", "root", "111111", "cloud2"]}
    return tns