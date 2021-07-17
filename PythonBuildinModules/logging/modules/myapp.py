import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log',level=logging.INFO)
    logging.info('started')
    mylib.do_something()
    logging.info('end')

if __name__ == '__main__':
    main()
