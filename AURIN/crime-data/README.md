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

### crime data
```json
{
    "lga_code": {
        "crimes": {"crime": crime count}
        "lga_name": "name for lga_code"
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

#### all "crime"
```
['a40_abduction_and_related_offences',
 'b30_burglary_break_and_enter',
 'a10_homicide_and_related_offences',
 'f30_other_government_regulatory_offences',
 'total_division_c_offences',
 'a30_sexual_offences',
 'a70_stalking_harassment_and_threatening_behaviour',
 'e10_justice_procedures',
 'total_division_f_offences',
 'a50_robbery',
 'b50_deception',
 'b20_property_damage',
 'c30_drug_use_and_possession',
 'total_division_a_offences',
 'd30_public_nuisance_offences',
 'reference_period',
 'b10_arson',
 'total_division_d_offences',
 'c20_cultivate_or_manufacture_drugs',
 'f90_miscellaneous_offences',
 'd20_disorderly_and_offensive_conduct',
 'd40_public_security_offences',
 'a80_dangerous_and_negligent_acts_endangering_people',
 'total_division_b_offences',
 'd10_weapons_and_explosives_offences',
 'total_division_e_offences',
 'e20_breaches_of_orders',
 'f10_regulatory_driving_offences',
 'a60_blackmail_and_extortion',
 'b40_theft',
 'c90_other_drug_offences',
 'f20_transport_regulation_offences',
 'a20_assault_and_related_offences',
 'b60_bribery',
 'c10_drug_dealing_and_trafficking']
```
