from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = 'Lattice'
    VERSION: str = '0.0.1'
    ROOT_PATH: str = ''
    CORS_ORIGINS: str = '*'

    ###########################################
    ############ Elastic Config ###############
    ###########################################

    ELASTIC_URL = 'http://localhost:9200'
    NODE_INDEX: str = 'nodes'
    EDGE_INDEX: str = 'edges'

    class Config:
        env_file = '.env'

settings = Settings()