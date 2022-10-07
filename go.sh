#! /bin/bash -
# Check if another instance of script is running
if pidof -o %PPID -x -- "$0" >/dev/null; then
  printf >&2 '%s\n' "ERROR: Script $0 already running"
  exit 1
fi
cd "$(dirname "$0")"
python ./bitscanner.py || python2 ./bitscanner.py || python3 ./bitscanner.py
