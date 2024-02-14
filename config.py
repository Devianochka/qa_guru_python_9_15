from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    window_width: str = '1900'
    window_height: str = '1028'
    base_url: str = 'https://megamarket.ru/'
    remote: bool = False
    page_load_strategy: str = 'normal'
    selenoid_capabilities: dict = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
