# 433 Remote Automation
By Paul Happy Hutchinson

__Note:__ This has only been tested with a Raspberry Pi 3B but it will likely work on all Raspberry Pi's and more.

__Note:__ This only works when the code the remote transmits is always the same (but you can still use it to recieve/record anything message allowing you to reverse engineer if needs be)

## Background
I wanted to open and close my electric gates by emulating the signal sent from my handheld remote so that I could then open and close the gates from anywhere using a web based interface (which is not included in this repo, this repo is 433 stuff only). I took inspiration from an Instructable, which is mentioned in the credits, then improved it by removing the need to understand what the actual message been trasmitted once (so no reverse engineering required) and improove the receiving script (orginally it logged the `1`s and `0`s as fast as it could whereas I changed it to log only when `1`s and `0`s changed).

## Usage
First you need to use the receive script to get the message your remote is sending. This will give you a CSV file which you can optionally use to graph and understand the message. You can also use it to tidy up the message (trim the recording, remove noise and so on). Next you need to send the message to test it works. If it did, yay you can now use it in your projects. If it didn't work then try again, if the code changes with each use of the remote, then you will need to reverse engineer it - have fun!

### Arguments
 - `pin` is the `GPIO` pin number to use
 - `time` is the length to receive for (in seconds)
 - `file` is the `file` to read/write from

### Receive
`python2.7 receive.py (PIN) (TIME) (FILE)`

### Send
`python2.7 send.py (PIN) (FILE)`

## Credits
Thank you to you awesome people!

### [george7378](http://www.instructables.com/member/george7378/) from [Instructables](http://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/?ALLSTEPS)
For inspiration for the project and also part of the receive.py script.
