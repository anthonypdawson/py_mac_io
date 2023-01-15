PyMacIO

Interface with the [macaddress.io](http://macaddress.io) API 

 _Note: there is a '5 minute' script version in ./script that I would write for myself in a time crunch_

# Configuration #
The macaddress.io API key is stored in an environment file (or optionally as an environment variable)
1. Create your configuration file
   1. `cp .env.local .env`
2. Add your macaddress.io api key where indicated in the sample file
3. The API url is predefined and should not need to be changed


You can also set the following environment variables:
- MACIO_API_KEY
- MACIO_API_URL

# Run from Docker image #

1. Navigate to project root
2. `docker build -t pymacio .`
3. Run pymacio _(using example address 00:00:00:00:00:00)_
   1. See usage: `docker run pymacio -h`
   2. Query company name: `docker run pymacio 00:00:00:00:00:00`
   3. Dump entire JSON response: `docker run pymacio --full 00:00:00:00:00:00`
   4. Accepts address with colons, dashes or no delimiter


# Running locally #

1. Install Python (>=3.9.6)
2. Install curl
   1. Examples
      1. Linux: `apt-get install curl`
      2. MacOS: `brew install curl` 
3. Install poetry 1.3.2 and add to path
   1. `curl -sSL https://install.python-poetry.org | python - --version 1.3.2`
   2. `export PATH="$POETRY_HOME/bin:$PATH"`
4. Run the app
   1. To see usage: `poetry run pymacio -h`
   2. Query company name: `poetry run pymacio 00:00:00:00:00:00`
   3. Dump entire JSON response: `poetry run pymacio --full 00:00:00:00:00:00`
