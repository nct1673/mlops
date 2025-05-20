from logger import logging

def fn(msg):
    logging.debug('This is logging debug message')
    print(msg)

fn("well done")