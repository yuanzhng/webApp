CONFIG_PATH = "C:\webApp\webApp\config.txt"

def read_config():
    config = {}
    with open(CONFIG_PATH, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

config = read_config()