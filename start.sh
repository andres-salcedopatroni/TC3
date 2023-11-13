sudo apt-get install python3.7

# Exit early on errors
set -eu

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# Install Python 3 virtual env
VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
  python3 -m venv $VIRTUALENV
fi

# Install the requirements
$VIRTUALENV/bin/pip install -r requirements.txt

# Run a glorious Python 3 server
$VIRTUALENV/bin/python3 app.py