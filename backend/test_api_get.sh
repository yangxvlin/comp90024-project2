# shellcheck disable=SC2140
LOCATION="{"""location""":"""Read a book"""}"
read -p "Enter server url: " url
curl -i "$url"/map

curl -i -H "Content-Type: application/json" -X GET -d "{\"location\":1}"  "$url"/map
