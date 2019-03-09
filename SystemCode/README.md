## Build Setup

Installation Requirements:
- [Anaconda](https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe "Anaconda") / [Python 3.6](https://www.python.org/downloads/release/python-365/ "Python 3.6") or older
- [Node.js ](https://nodejs.org/en/ "Node.js ")
- Microsoft Visual C++ 14.0: [Build Tools for Visual Studio 2017](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15 "Build Tools for Visual Studio 2017")  

``` bash
# install all front end dependencies
cd web/
npm install

# install all backend dependencies
pip install requests flask flask_cors durable_rules

# run start.bat to start all application
start.bat

# access localhost:8080/home

```
