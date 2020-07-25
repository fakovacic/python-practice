# Requirements

Python 3.8.3 or newer (older versions could work)  
Latest version of flask  
No app running on port 8080  

# Endpoints

/ -> returns the list of all possible endpoints  
/up -> takes 1 number as an argument and returns a json rounded to the ceiling (or the same number if int), otherwise raises an appropriate error  

# Usage

If pipenv is installed locally you can use pipenv install to quickly create an enviroment from the pipfile  

Otherwise create a new venv and run:  

pip install flask  
python api.py  

Application is running on http://localhost:8080


##TODO

make Dockerfile to containerize the app
