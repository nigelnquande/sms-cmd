#!/usr/bin/env python3

# Command-line client of SMS CMD

from sys import argv, stderr, stdout, exit

try:
  """Import libs necessary to talk to the server, which always runs and keeps track of msgs sent per day, 
    so as to limit abuse/spam to 100 max."""
except ImportError:
  stderr.write("Could not import twilio.com REST API. Please install it.")
  


# main execution of smscmd client happens here

def main():
  # Mainline logic happens here

if __name__ == "__main__":
  main()
