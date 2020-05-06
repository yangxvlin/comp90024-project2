# population-age

## how to run
```python main.py```
- if you add more json file, just add the file name in ```data_file.json``` and rerun the python script and result file will be ready

## format
### meta
```json
{
    table attribute name short cut: {
        "title": "table attribute name ",
        "description": "What does the attribute mean"
    }
}
```

### population age data
```json
{
    "lga_code": {
        "total_population": total population,
        "count": {"age group":  age group population count}, 
        "percent": {"age group":  age group population percent}
    },
}

```

#### all "lga_code"
```
["Greater Adelaide"
"Greater Melbourne"
"Greater Brisbane"
"Greater Sydney"]
```

#### all "count"
```
['_75_79_yrs_proj_count',
 '_40_44_yrs_proj_count',
 '_25_29_yrs_proj_count',
 '_0_4_yrs_proj_count',
 '_10_14_yrs_proj_count',
 '_80_84_yrs_proj_count',
 '_70_74_yrs_proj_count',
 '_5_9_yrs_proj_count',
 '_50_54_yrs_proj_count',
 '_15_19_yrs_proj_count',
 '_35_39_yrs_proj_count',
 '_30_34_yrs_proj_count',
 '_85_yrs_over_proj_count',
 '_20_24_yrs_proj_count',
 '_45_49_yrs_proj_count',
 '_55_59_yrs_proj_count',
 '_60_64_yrs_proj_count',
 '_65_69_yrs_proj_count']

```

#### all "percent"
```
['_85_yrs_over_proj_percent',
 '_60_64_yrs_proj_percent',
 '_35_39_yrs_proj_percent',
 '_25_29_yrs_proj_percent',
 '_50_54_yrs_proj_percent',
 '_40_44_yrs_proj_percent',
 '_5_9_yrs_proj_percent',
 '_15_19_yrs_proj_percent',
 '_55_59_yrs_proj_percent',
 '_70_74_yrs_proj_percent',
 '_75_79_yrs_proj_percent',
 '_0_4_yrs_proj_percent',
 '_30_34_yrs_proj_percent',
 '_80_84_yrs_proj_percent',
 '_45_49_yrs_proj_percent',
 '_65_69_yrs_proj_percent',
 '_20_24_yrs_proj_percent',
 '_10_14_yrs_proj_percent'])
```
