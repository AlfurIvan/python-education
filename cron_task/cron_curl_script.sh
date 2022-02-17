#! /bin/bash
curl -o cron_task_outputJSON.json "https://api.openweathermap.org/data/2.5/weather?lat=48.6208&lon=22.2879&appid={e1e87ea5e71fb7f0fe92439f99ecc528}"
# 0 12 * * * bash /home/kvitravn/cron_curl_script.sh
