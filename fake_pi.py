import random
import time
import requests

# HAN_ADDRESS = 'http://35.225.138.161'
HAN_ADDRESS = 'http://0.0.0.0' # Localhost for testing


def main():
    while True:
        voltage_reading = random.random() * 5
        requests.post(HAN_ADDRESS + '/push_data', data={'voltage': voltage_reading})
        print('Sent!')
        time.sleep(1)

if __name__ == '__main__':
    main()
