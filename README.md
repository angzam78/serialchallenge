### Serial Challenge

Serial comms demo with threading on Python.

## Description

This software will:
- Discover and print to screen all available COM ports
  - gracefully fail (print error message to screen) if not enough COM ports are available
- Create two threads; 
  - first thread connects to first COM port and writes serial data to it
  - second thread connects to the other COM port then reads the serial data and prints it to screen

## Prerequisites

A pair of connected COM ports is required for this software to work (for example: COM1 port connected to COM2 port). If physical COM ports are not available then a virtual serial port emulator will work too. 

To have a virtual serial port emulator on Windows 10 install [com0com](https://sourceforge.net/projects/com0com/files/latest/download). This will create the required a connected virtual COM port pair by default.

## Install and run

```
C:\MyWorkspace> git clone https://github.com/angzam78/serialchallenge.git
C:\MyWorkspace> cd serialchallenge
C:\MyWorkspace\serialchallenge> pip install -r requirements.txt
C:\MyWorkspace\serialchallenge> python3 serialchallenge.py
```
### Example run

```
C:\MyWorkspace\serialchallenge> python3 serialchallenge.py
Starting serialchallenge (angzam78)...
Found 2 COM ports ('COM4', 'COM8')
Setting up I/O handling threads
Data will be sent on COM4 and received on COM8
Press CTRL+C to interrupt loop...
Starting in 9 8 7 6 5 4 3 2 1 0 PUGeDvGc61SWjgjEbjl33uAvxeO3LZPRPmCyJ75Z3fPHnNcwb5sSdDp0vfyUuG3wAqEVgk0sCtUfX0jyOIC6BIi8MIMq3mJxWx0yxdWqFCOcnMitB9eOKo2jQfDdlZNR2Bd2DcSF6hq1UZU5zHl1tEe5ODrN25GX3TayQLG1E0JPxRPyaz5XJemvy2b80tIsQb1lMEK663WzEjBJV7eKU6tyhG703pzqM1oOv3J1SQW6lRJKqE8obK2zbWJIGVnjXPyy3IDuXJ4L4tUrPioqazG5Ml8uwYKxOqJCQAfrjnhdbUzUeRqxwuy3F14pCM94mDQKlw2QQJfEhg2nzvWn90p2gr35zBOUX9xCwP3l9y1oXYbPzwNLA2smx5zta...
XHYy8RyDOibQVJzcWSQcihP4upo4tT2hbLxWSGdAurqQ6VZuHBhmMyADJsuMx25aR4J1MY0g9GhkFhK97x1Ub5Rv6rFSAm2I8qhLJYOT2X2NLDhiPsA1iLIKRSqzqRDbmpYYDlTK2ZxFpdEoBaSRAzjHWYY5D6TtiSXnRJYU5GnL17SivlggKhwt6a0NuVHEcQGev5n5Sf3mfTxME34UKStup9MrJmpBEMDUsEXirXCEaghViaq9890Hn3C16MwxEi7c2ieaIPYvXHg
Loop interrupted, stopping I/O threads...
hNQ82SEDLxUOtWz1t3rJ0kZyvPLKzdjVSbqRuGZ9SJjP7M3uqSX
Done!
```

#### Note

When the program is interrupted by the user any data that is still being processed is printed to screen before the program finishes. This was left on purpose to demonstrate how the program finishes processing all the received data before exiting instead of simply halting everything when the user stops the program.
