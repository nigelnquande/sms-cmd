#!/usr/bin/env python3

# Read http://www.souravsengupta.com/int2pro2014/python/LPTHW.pdf and
# http://stock.ethop.org/pdf/python/Learning%20Python,%205th%20Edition.pdf for getting up to spead with Python
# See https://xkcd.com/353/ for why you should.

# Command-line client of SMS CMD

from sys import argv, stderr, stdout, exit

try:
  """Import libs necessary to talk to the server, which always runs and keeps track of msgs sent per day, 
    so as to limit abuse/spam to 100 max."""
except ImportError:
  stderr.write("Could not import module X. Please install it.")
  


# main execution of smscmd client happens here

def main():
  # Mainline logic happens here
  # do some arsing of command line arguments

if __name__ == "__main__":
  main()
