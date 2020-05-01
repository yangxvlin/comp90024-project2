# income

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

### income data
```json
{
    "lga_code": {
        "lga_name": "name for lga_code",
        "total": total houshold, 
        "income": {"income range":  income}, 
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
 '22830',
 '22910',
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
 '22490',
 '22620',
 '22670',
 '22750',
 '25060',
 '25150',
 '22310',
 '22410',
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
 '27630',
 '29399']
```

#### income
```
['hi1500_1999_tot_hhlds',
 'hi3000_more_tot_hhlds',
 'hi150_299_tot_hhlds',
 'hi650_799_tot_hhlds',
 'hi500_649_tot_hhlds',
 'hi1000_1249_tot_hhlds',
 'hi1_149_tot_hhlds',
 'hi400_499_tot_hhlds',
 'hi1250_1499_tot_hhlds',
 'hi300_399_tot_hhlds',
 'hi800_999_tot_hhlds',
 'all_income_ns_other_household',
 'hi2000_2499_tot_hhlds',
 'hi2500_2999_tot_hhlds']
```
