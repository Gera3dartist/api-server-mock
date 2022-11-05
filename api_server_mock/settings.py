from functools import lru_cache
import pathlib
from pymlconf import Root


config_dir = pathlib.Path(__file__).parent.resolve()


@lru_cache()
def get_settings() -> Root:
    config = Root()
    for conf_file in [
        config_dir/'config.yaml', 
        config_dir/'.local.yaml'
    ]:
        if conf_file.exists():
            config.loadfile(str(conf_file))
    return config
    

config = get_settings()
