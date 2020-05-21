# income

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
        "income range": count,
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

#### all "income range"
```
[
'hi_1_149_tot',
'hi_150_299_tot',
'hi_300_399_tot',
'hi_400_499_tot',
'hi_500_649_tot',
'hi_650_799_tot',
'hi_800_999_tot',
'hi_1000_1249_tot',
'hi_1250_1499_tot',
'hi_1500_1749_tot',
'hi_1750_1999_tot',
'hi_2000_2499_tot',
'hi_2500_2999_tot',
'hi_3000_3499_tot',
'hi_3500_3999_tot',
'hi_4000_more_tot',
]
```
