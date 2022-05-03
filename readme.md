# Install venv
Once installed python3, open a console and run the following:
```bash
sudo apt-get install python3-pip #install pip3
python3 -m pip install virtualenv    #install virtualenv
virtualenv -p python3 venv #create a virtualenv named venv
source venv/bin/activate    #Active virtualenv
```
When the test is over, run:
```bash
deactivate
```
# Install python requirements
```bash
python3 -m pip install -r requirements.txt
```

# Usage
```bash
python3 run.py
```
* Open your browser and go to: http://localhost:5000

* Navegate through the web page and enjoy

# Technologies used
* Python 3.8.10
* Twitter API v2: https://developer.twitter.com/en/docs/twitter-api
* Flask 2.1.1
* Postman
* Beekeeper-studio
* MySql

## This API took  24 hours to be completed