import mysql.connector
import yaml
import os

THIS_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(THIS_PATH, 'config.yml')

def get_config(config_file_path):
    config={}
    try:
        with open(config_file_path, "rt") as conf:
            config = yaml.safe_load(conf)
    except(FileNotFoundError):
        print(f"No existeix cap fitxer de configuració: {config_file_path}")
    return config

def db_client():

    try:
        config = get_config(CONFIG_PATH)

        return mysql.connector.connect(
            user=config['base de dades']['user'],
            password=config['base de dades']['password'],
            host=config['base de dades']['host'],
            port=config['base de dades']['port'],    
            database=config['base de dades']['database']
        )
    
    except Exception as e:
        return {"status": -1, "message": f"Error de conexió:{e}"}
