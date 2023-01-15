PyMacIO

Interface with the [macaddress.io](http://macaddress.io) API 

# Configuration #
1. Create your configuration file
   1. `cp .env.local .env`
2. Add your macaddress.io api key where indicated in the sample file
3. The API url is predefined and should not need to be changed


# Quick guide to run locally #

1. Install Python (>=3.9.6)
2. Install curl
   1. Typically - Linux: `apt-get install curl`, MacOS: `brew install curl` 
3. Install poetry 1.3.2 and add to path
   1. `curl -sSL https://install.python-poetry.org | python - --version 1.3.2`
   2. `export PATH="$POETRY_HOME/bin:$PATH"`
4. Run the app
   1. To see usage: `poetry run pymacio -h`
   2. Accepts mac address with or without colons
   3. Query company name: `poetry run pymacio 00:00:00:00:00:00` where 00:00:00:00:00:00 is the address to check.
   4. Do not filter to company name: `poetry run pymacio --full 00:00:00:00:00:00`

# Build Docker image #

1. Navigate to project root
2. `docker build -t pymacio .`
3. Run pymacio
   1. `docker run `