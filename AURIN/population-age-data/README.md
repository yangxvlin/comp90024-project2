# crime

## how to run
```python main.py```
- if you add more crime json file, just add the file name in ```data_file.json``` and rerun the python script and result file will be ready

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
        "lga_name": "name for lga_code",
        "total_population": total population,
        "count": {"age group":  age group population count}, 
        "percent": {"age group":  age group population percent}
    },
}

```

#### all "lga_code"
```
['20110',
 '20260',
 '20570',
 '20660',
 '20740',
 '20830',
 '20910',
 '21010',
 '21110',
 '21180',
 '21270',
 '21370',
 '21450',
 '21610',
 '21670',
 '21750',
 '21830',
 '21890',
 '22110',
 '22170',
 '22250',
 '22410',
 '22490',
 '22620',
 '22750',
 '22830',
 '22910',
 '22670',
 '22310',
 '22980',
 '23110',
 '23190',
 '23270',
 '23350',
 '23430',
 '23670',
 '23810',
 '23940',
 '24130',
 '24210',
 '24250',
 '24330',
 '24410',
 '24600',
 '24650',
 '24780',
 '24850',
 '24900',
 '24970',
 '25060',
 '25150',
 '25250',
 '25340',
 '25430',
 '25490',
 '25620',
 '25710',
 '25810',
 '25900',
 '25990',
 '26080',
 '26170',
 '26260',
 '26350',
 '26430',
 '26490',
 '26610',
 '26670',
 '26700',
 '26730',
 '26810',
 '26890',
 '26980',
 '27070',
 '27170',
 '27260',
 '27350',
 '27450',
 '27630']
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
