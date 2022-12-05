import logging


if __name__ == "__main__":
    
    logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG, format='%(levelname)')
    logging.info("Starting server")