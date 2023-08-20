import yaml
from typing import Dict


def read_config(path: str) -> Dict:
    config: Dict
    # Read from YAML file
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config
