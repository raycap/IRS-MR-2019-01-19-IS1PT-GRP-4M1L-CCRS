## Build Setup

Requirements:
* nodejs and npm should be installed. Otherwise please download and install from the following website: https://www.npmjs.com/get-npm
* Python 2.7 ~ Python 3.6.5 should be installed. Otherwise, please download and install from the following website: https://www.python.org/downloads/ 

Installation:
- [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe "Anaconda") / [Python 3.6](https://www.python.org/downloads/release/python-365/ "Python 3.6") or older
- [Node.js ](https://nodejs.org/en/ "Node.js ")
- Microsoft Visual C++ 14.0: [Build Tools for Visual Studio 2017](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15 "Build Tools for Visual Studio 2017")  

``` bash
# 1. install all front end dependencies
cd web/
npm install

# 2. install all backend dependencies
pip install requests flask flask_cors durable_rules

# 3. (Windows only) run start.bat to start all application 
./start.bat
# 3. (Non windows) you need to run redis server manually, and then run the rules engine by running cc_system.py inside rules-engine folder 
python cc_system.py


# 4. Try access localhost:8080/home 


# Alternatively you just need to run rules engine by running python script and redis
start_server.bat
# And then access the frontend from AWS host. This static host will connect to your localhost rules engine backend
http://machine-reasoning.s3-website-ap-southeast-1.amazonaws.com/home


```
