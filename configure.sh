#!/bin/bash

VIRTUALENV="$(pwd -P)/.venv"
EXAMPLE_ENVFILE="$(pwd -P)/example.env"
PYTHON="${PYTHON:-python3}"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Validate the minimum required Python version
COMMAND="${PYTHON} -c 'import sys; exit(1 if sys.version_info < (3, 12) else 0)'"
PYTHON_VERSION=$(eval "${PYTHON} -V")

eval $COMMAND || {
  echo -e "$RED ---------------------------------------------------------------------------------$NC"
  echo -e "$RED ERROR: Unsupported Python version: ${PYTHON_VERSION}. Patient Management requires$NC"
  echo -e "$RED Python 3.12 or later. To specify an alternate Python executable, set the PYTHON$NC"
  echo -e "$RED environment variable. For example:$NC"
  echo -e "$RED $NC"
  echo -e "$RED   sudo PYTHON=/usr/bin/python3.12 ./configure.sh$NC"
  echo -e "$RED $NC"
  echo -e "$RED To show your current Python version: ${PYTHON} -V$NC"
  echo -e "$RED ---------------------------------------------------------------------------------$NC"
  exit 1
}
echo "Using ${PYTHON_VERSION}"

# Remove the existing virtual environment (if any)
if [ -d "$VIRTUALENV" ]; then
  COMMAND="rm -rf \"${VIRTUALENV}\""
  echo -e "$GREEN Removing old virtual environment ...$NC"
  eval $COMMAND
else
  echo -e "$YELLOW No virtual environment to remove. Continuing ...$NC"
  WARN_MISSING_VENV=1
fi


# Create a new virtual environment
COMMAND="${PYTHON} -m venv \"${VIRTUALENV}\""
echo -e "$GREEN Creating a new virtual environment at ${VIRTUALENV} ...$NC"
eval $COMMAND || {
  echo "--------------------------------------------------------------------"
  echo "ERROR: Failed to create the virtual environment. Check that you have"
  echo "the required system packages installed and the following path is"
  echo "writable: ${VIRTUALENV}"
  echo "--------------------------------------------------------------------"
  exit 1
}

# Activate the virtual environment
source "${VIRTUALENV}/bin/activate"

# Upgrade pip
COMMAND="pip install --upgrade pip"
echo -e "$GREEN Updating pip ($COMMAND)...$NC"
eval $COMMAND || exit 1
pip -V

# Install required Python packages
COMMAND="pip install -r requirements-dev.txt"
echo -e "$GREEN Installing development dependencies ($COMMAND)...$NC"
eval $COMMAND || exit 1

COMMAND="pip install -r requirements.txt"
echo -e "$GREEN Installing application dependencies ($COMMAND)...$NC"
eval $COMMAND || exit 1

# Installation of pre-commit
COMMAND="pre-commit install"
echo -e "$GREEN Installing pre-commit hooks...$NC"
eval $COMMAND || exit 1

# Set environment file
COMMAND="cp $EXAMPLE_ENVFILE $(pwd -P)/.env"
if [ ! -s "$(pwd -P)/.env" ]; then
  echo -e "$GREEN Creating .env file ...$NC"
  eval $COMMAND || exit 1
elif [ -f "$(pwd -P)/.env" ]; then
  echo -e "$YELLOW Skipping set environment variables (.env file are populated)$NC"
fi

echo -e "$GREEN --------------------------------------------------------------------$NC"
echo -e "$GREEN Confiruation complete! You can start your development after set the$NC"
echo -e "$GREEN environment variables at:$NC"
echo "  ./.env"
echo -e "$GREEN Don't forget to apply the migrations:$NC"
echo "  > make migrate"
echo -e "$GREEN --------------------------------------------------------------------$NC"
