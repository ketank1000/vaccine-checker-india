#!/usr/bin/env python3
"""
Find vaccine appointments at your location.
This script uses api looking for vaccine appointments in the pincode you specify.
:author: ketan khandagale
:date: May 2021
"""

import argparse
import requests
import pyttsx3
import pprint
import time, datetime


#set defaults
date_list = []
url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?'

# set date
delta = datetime.timedelta(days=1)
today = datetime.date.today()

# set headers
headers= {
    'accept': 'application/json',
    'Accept-Language': 'hi_IN',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

# set objs
pp = pprint.PrettyPrinter(indent=4)
engine = pyttsx3.init()

# set voice settings
voices = engine.getProperty('voices')
engine.setProperty('volume',1.0) 
engine.setProperty('voice', voices[33].id)


def main():

    # set up an argument parser
    parser = argparse.ArgumentParser(prog='vaccine.py')
    parser.add_argument("--total",
                        dest="total_hours",
                        type=int,
                        help="Total Number of hours for which to run the script",
                        default=3)
    parser.add_argument("--pincode",
                        help="PinCode of place to check availability",
                        type=int,
                        required=True)
    parser.add_argument("--days",
                        help="No. of days to check availability for (default=1)",
                        type=int,
                        default=1)
    parser.add_argument("--age-limit",
                        dest="age_limit",
                        type=int,
                        help="Age limit for taking vaccine (default=18)",
                        default=18)
    parser.add_argument("--date",
                        help="Specific date to check availability for (frt='dd-mm-yyyy')",
                        type=str,
                        default=None)

    # parse given command line arguments
    args = parser.parse_args()
    max_time = time.time() + args.total_hours * 60 * 60
    if args.date:
        date_list.append(args.date)
    else:
        for single_date in (today + datetime.timedelta(days=n) for n in range(args.days)):
            date_list.append(single_date.strftime("%d-%m-%Y"))

    # run for given time
    while time.time() < max_time:
        try:
            available_centers = []
            for date in date_list:
                format_url = f"{url}pincode={args.pincode}&date={date}"
                r=requests.get(url=format_url,headers=headers)
                if (r.status_code == 200):
                    output = r.json()
                    for center in output['centers']:
                        for session in center['sessions']:
                            if session['available_capacity'] > 0 and session['min_age_limit'] >= args.age_limit:
                                available_centers.append({center['name']:f"{session['available_capacity']} available on {date}"})
                else:
                    print(f"Failed with {r.status_code}")
            if available_centers:
                print(available_centers)
                engine.say("Your vaccine slot is available. Please check and do registration.")
                engine.runAndWait()
            else:
                print(f"No slots available yet in {', '.join(date_list)}")
            time.sleep(60)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()