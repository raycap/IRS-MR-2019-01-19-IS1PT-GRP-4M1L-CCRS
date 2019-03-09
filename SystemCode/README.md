## Build Setup

Requirements:
* nodejs and npm should be installed. Otherwise please download and install from the following website: https://www.npmjs.com/get-npm
* Python 2.7 ~ Python 3.6.5 should be installed. Otherwise, please download and install from the following website: https://www.python.org/downloads/ 

Installation:
- [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe "Anaconda") / [Python 3.6](https://www.python.org/downloads/release/python-365/ "Python 3.6") or older
- [Node.js ](https://nodejs.org/en/ "Node.js ")
- Microsoft Visual C++ 14.0: [Build Tools for Visual Studio 2017](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15 "Build Tools for Visual Studio 2017")  

``` bash
# install all front end dependencies
cd web/
npm install

# install all backend dependencies
pip install requests flask flask_cors durable_rules

# run start.bat to start all application (Windows only)
start.bat

# try access localhost:8080/home

# alternatively you just need to run rules engine by running python script and redis (Windows only)
start_server.bat

# and access the frontend from AWS host
http://machine-reasoning.s3-website-ap-southeast-1.amazonaws.com/home

```
