# configurations/config.py

class BaseConfig:
    TIMEOUT = 10


class StagingConfig(BaseConfig):
    BASE_URL = "https://www.staging.automationexercise.com"  # This is example URL just to showcase
    ENV_NAME = "Staging"


class QAConfig(BaseConfig):
    BASE_URL = "https://qa.automationexercise.com"  # This is example URL just to showcase
    ENV_NAME = "QA"


class ProdConfig(BaseConfig):
    BASE_URL = "https://automationexercise.com"
    ENV_NAME = "Production"
