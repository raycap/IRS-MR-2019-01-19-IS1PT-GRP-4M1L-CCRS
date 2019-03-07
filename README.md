## Build Setup

``` bash
# install all front end dependencies
cd web/
npm install

# install all backend dependencies
pip install requests, flask, flask_cors, durable_rules

# locate the path of redis config and change set it in start_redis.bat
start_redis.bat :
redis-server "C:\Program Files\Redis\redis.windows.conf" <- change this

# run start.bat to start all application
start.bat

# access localhost:8000/home

```
