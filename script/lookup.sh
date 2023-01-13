#!/usr/bin/env sh

MAC_ADDRESS=$1

MAC_REGEX="^([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}$"

if ! [[ $MAC_ADDRESS =~ $MAC_REGEX ]]; then
  echo "MAC address invalid"
  exit 1
fi

FULL_URL="${MACIO_API_URL}?apiKey=${MACIO_API_KEY}&output=json&search=${MAC_ADDRESS}"


[ -d "./output" ] || mkdir "output"
STRIPPED_MAC=$(echo ${MAC_ADDRESS} | sed 's/://g')
RESP_FILE="./output/${STRIPPED_MAC}.txt"
echo "Storing full responsen to ${RESP_FILE}"
curl "${FULL_URL}" -o "${RESP_FILE}"
cat "${RESP_FILE}"

