#!/usr/bin/env python

"""
File: serialchallenge.py
Author: Angelo Zammit (angzam78)
Date: 2023-09-21
Description: Serial communication over connected COM ports.
"""

import sys
import time
import serial
import serial.threaded
import random, string
import traceback

from serial.tools import list_ports

sys.stdout.write("Starting serialchallenge (angzam78)...\n")

# discover all available COM ports
ports = sorted(list_ports.comports())

# gracefully fail if no COM ports are available (or if there is only one)
match len(ports) :
    case 1: 
        sys.exit("At least two COM ports are required (only 1 found)... exiting\n")
    case 0: 
        sys.exit("No COM ports found... exiting\n")

# print to screen all available COM ports
sys.stdout.write("Found {} COM ports {}\n".format(len(ports), next(zip(*ports))))

# a basic raw data connection handler
class ConnectionHandler(serial.threaded.Protocol):
    
    def connection_made(self, transport):
        self.transport = transport
        self.port = transport.serial.port

    def data_received(self, data):
        sys.stdout.write(data.decode('utf-8'))

    def connection_lost(self, exc):
        if exc:
            traceback.print_exc(exc)

# hardcoded COM port selection
# TODO: let user specify which COM ports to use
port_send = ports[0][0] # first COM port
port_recv = ports[1][0] # other COM port

# create two threads... 
# first thread connects to first COM port and writes serial data to it
# second thread connects to the other COM port; reads the serial data and prints it to screen
sys.stdout.write("Setting up I/O handling threads")

# set up pyserial threads
write_thread = serial.threaded.ReaderThread(serial.serial_for_url(port_send), ConnectionHandler)
read_thread = serial.threaded.ReaderThread(serial.serial_for_url(port_recv), ConnectionHandler)

# start threads
write_thread.start()
read_thread.start()

# wait for threads to connect to COM ports
write_thread.connect()
read_thread.connect()

# user instructions
sys.stdout.write("Data will be sent on {} and received on {}\n"
    .format(write_thread.protocol.port, read_thread.protocol.port))
sys.stdout.write("Press CTRL+C to interrupt loop...\n")

# main section
try:
    # countdown before sending data 
    sys.stdout.write("Starting in ")
    for countdown in reversed(range(10)):
        sys.stdout.write("{} ".format(countdown))
        time.sleep(1)
    else:
        sys.stdout.write("\n")
    
    # main loop
    while True:
        ascii_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        write_thread.write(random.choice(ascii_chars).encode('ascii'))

# wait for user to stop program
except KeyboardInterrupt:
    sys.stdout.write('\nLoop interrupted, stopping I/O threads...\n')

# close COM ports, stop threads 
# and wait for threads to finish
write_thread.close()
write_thread.join()

# read thread finishes last 
read_thread.close()
read_thread.join()

sys.stdout.write("\nDone!\n")
