@echo off
START "redis" /min start_redis.bat ^& exit
@echo off
START "rules engine" /min start_rules_engine.bat ^& exit
exit