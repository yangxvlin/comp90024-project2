require 'csv'
require 'json'
require 'time'

data = {
  fields: [
    {name: 'country', format: '', type: 'string'},
    {name: 'state', format: '', type: 'string'},
    {name: 'day', format: 'YYYY-M-D H:m:s', type: 'timestamp'},
    {name: 'latitude', format: '', type: 'real'},
    {name: 'longitude', format: '', type: 'real'},
    {name: 'count', format: '', type: 'integer'},
  ],
  rows: []
}

CSV.foreach("covid19.csv", {headers: true}) do |row|
  data[:rows] << [
    row["Country/Region"].to_s,
    row["Province/State"].to_s,
    Time.parse(row["Date"]).to_s,
    row["Lat"].to_f,
    row["Long"].to_f,
    row["Value"].to_i
  ]
end

File.open("covid19.json", "w") do |file|
  file.puts data.to_json
end