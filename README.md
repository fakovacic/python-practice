# v1.0.0

## Requirements

Python 3.8.3 or newer (older versions could work)  
Latest version of flask  
No app running on port 8080  

## Install

1. pip `sudo apt install python-pip`
2. run `python api.py`

## Endpoints

/ -> returns the list of all possible endpoints  
/up -> takes 1 number as an argument and returns a json rounded to the ceiling (or the same number if int), otherwise raises an appropriate error  
