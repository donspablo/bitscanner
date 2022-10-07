#! /bin/bash -
# Check if another instance of script is running
if pidof -o %PPID -x -- "$0" >/dev/null; then
  printf >&2 '%s\n' "ERROR: Script $0 already running"
  exit 1
fi
cd "$(dirname "$0")"
./memcached -n 70 -m 5200 -M -t 12 || memcached -n 70 -m 5200 -M -t 12 &
python ./bit.py || python2 ./bit.py || python3 ./bit.py