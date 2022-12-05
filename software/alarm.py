from dataclasses import dataclass
from datetime import datetime
import logging


class Alarm:
    ...
    
    
@dataclass
class LogEintrag:
    zeitpunkt: datetime
    netzwerkname: str
    info_text: str
    wert: str
    
    def log(self):
        pass
    
    
class Messung:
    def __init__(self):
        pass
    
    def erfassen(self):
        pass
    
    
if __name__ == "__main__":
    
    logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Starting server")