import RPi.GPIO as GPIO
import csv
import sys
import time

PIN = int(sys.argv[1])
FILE = sys.argv[2]
PLAYBACK = [] # [[time, 1_OR_0, ...], ...]
PLAYBACK_SIZE = 0

if __name__ == '__main__':
    print '**Pin Setup**'
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)

    print '**Reading Playback**'
    with open(FILE, 'rb') as csvfile:
        rage = csv.reader(csvfile)
        lastTime = 0
        for row in rage:
            rowtime = float(row[0])
            row[0] = rowtime - lastTime
            lastTime = rowtime
            row[1] = float(row[1]) > 0.5
            PLAYBACK.append(row)
        PLAYBACK_SIZE = len(PLAYBACK);

    print '**Started Playback (', time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), ')**'
    for i in range(PLAYBACK_SIZE):
        GPIO.output(PIN, PLAYBACK[i][1])
        time.sleep(PLAYBACK[i][0])
    print '**Ended Playback (', time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), ')**'
    GPIO.cleanup()
