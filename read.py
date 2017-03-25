from datetime import datetime
import RPi.GPIO as GPIO
import csv

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 5
RECEIVE_PIN = 27
LAST = 0

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    cumulative_time = 0
    beginning_time = datetime.now()
    print '**Started recording**'
    while cumulative_time < MAX_DURATION:
        NOW = GPIO.input(RECEIVE_PIN)
        time_delta = datetime.now() - beginning_time
        if NOW != LAST:
           RECEIVED_SIGNAL[0].append(time_delta)
           RECEIVED_SIGNAL[1].append(LAST)
           time_delta = datetime.now() - beginning_time
           RECEIVED_SIGNAL[0].append(time_delta)
           RECEIVED_SIGNAL[1].append(NOW)
           LAST = NOW
        cumulative_time = time_delta.seconds
    print '**Ended recording**'
    print len(RECEIVED_SIGNAL[0]), 'samples recorded'
    GPIO.cleanup()

    print '**Processing results**'
    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds + RECEIVED_SIGNAL[0][i].microseconds/1000000.0

    print '**Plotting results**'
    with open('rage.csv', 'wb') as csvfile:
        rage = csv.writer(csvfile)
        for i in range(len(RECEIVED_SIGNAL[0])):
           rage.writerow([RECEIVED_SIGNAL[0][i], RECEIVED_SIGNAL[1][i]])
