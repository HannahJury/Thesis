import random
import time
import requests

# HAN_ADDRESS = 'http://104.154.231.147'
HAN_ADDRESS = 'http://0.0.0.0' # Localhost for testing
DEVICE_ID = 1


def main():
    while True:
        voltage_reading = random.random() * 5
        current_reading = random.random() * 0.01
        data = {'id': DEVICE_ID,
                'voltage': voltage_reading,
                'current': current_reading}
        print(data)
        requests.post(HAN_ADDRESS + '/push_data', data=data)
        print('Sent!')
        time.sleep(1)

if __name__ == '__main__':
    main()
