# shellcheck disable=SC2140
read -p "Enter server url: " url
read -p "Enter location id: " id
# shellcheck disable=SC2089
LOCATION="{\"location\":$id}"

# shellcheck disable=SC2090
curl -i -H "Content-Type: application/json" -X GET -d "$LOCATION" "$url"/map
