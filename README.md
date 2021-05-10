# vaccine-checker-india

Script to check availability of covid-19 vaccines in India with Voice alert. Voice alert is added as you can run the script in background. Once the slot is available you get the voice alert saying **"Your vaccine slot is available. Please check and do registration."** The script has feature to run for as many hours user wants.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install -r requirement.txt
```

## Help

```bash
python vaccine.py --help
usage: vaccine.py [-h] [--total TOTAL_HOURS] --pincode PINCODE [--days DAYS] [--age-limit AGE_LIMIT] [--date DATE]


optional arguments:
  -h, --help            show this help message and exit
  --total TOTAL_HOURS   Total Number of hours for which to run the script
  --pincode PINCODE     PinCode of to check availability
  --days DAYS           No. of days to check availability for (default=1)
  --age-limit AGE_LIMIT
                        Age limit for taking vaccine (default=18)
  --date DATE           Specific date to check availability for (frt='dd-mm-yyyy')
```

## Examples
Example 1: Checking availability for specific date
```bash
python vaccine.py --pincode 413102 --date 10-05-2021

[{'Baramati WH Local 18 To44 Only': '45 available on 10-05-2021'}]
```
Example 2: Checking availability for next 5 days
```bash
python vaccine.py --pincode 415537 --days 5 

[{'SC Adaraki (BIBI) PHALTAN': '9 available on 10-05-2021'}, {'PHC Bibi Covi': '25 available on 11-05-2021'}]
```


## License
[MIT](https://choosealicense.com/licenses/mit/)