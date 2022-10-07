#! /bin/bash -
# Check if another instance of script is running
if pidof -o %PPID -x -- "$0" >/dev/null; then
  printf >&2 '%s\n' "ERROR: Script $0 already running"
  exit 1
fi
cd "$(dirname "$0")"
pip install -r requirements.txt
cd ./app
python ./bitscanner.py || python2 ./bitscanner.py || python3 ./bitscanner.py || ./memcached -n 70 -m 5200 -M -t 12 || memcached -n 70 -m 5200 -M -t 12 &
python ./bitscanner.py || python2 ./bitscanner.py || python3 ./bitscanner.py