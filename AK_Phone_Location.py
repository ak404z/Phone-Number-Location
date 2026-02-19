#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ===============================================================
#  AK Software License v1.0
#  Copyright (c) 2025 AK (ak404z)
#
#  This software is provided for educational and research purposes
#  only. You are NOT allowed to use this code for:
#      - Illegal activities
#      - Harming individuals or organizations
#      - Unauthorized access or data breaches
#
#  By using this software, you agree that:
#      - The author is not responsible for any misuse.
#      - The tool is provided "AS IS" without any warranty.
#      - You assume full responsibility for any consequences.
#
#  You may modify and redistribute this code ONLY with proper
#  credit to the original author (AK / ak404z).
#
#  Unauthorized commercial use is strictly prohibited.
# ===============================================================
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import time

print('\033[1;32m===========================================================\033[0m')
print("\033[1;32m               AK Phone Number Location       \033[0m")
print('\033[1;32m            Telegram : https://t.me/AKServer404       \033[0m')
print('\033[1;32m            Github : https://github.com/ak404z        \033[0m')
print('\033[1;32m===========================================================\033[0m')

try:
    phone_number = input("\nPhone Number : ")

    print("\nRetrieving information..\n")

    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        status = "Valid" if phonenumbers.is_valid_number(parsed_number) else "Invalid"

        country_code = "+" + phone_number[1:3] if phone_number.startswith("+") else "None"
        
        try:
            operator = carrier.name_for_number(parsed_number, "fr")
        except:
            operator = "None"

        try:
            type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixed"
        except:
            type_number = "None"

        try:
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else "None"
        except:
            timezone_info = "None"

        try:
            country = phonenumbers.region_code_for_number(parsed_number)
        except:
            country = "None"

        try:
            region = geocoder.description_for_number(parsed_number, "fr")
        except:
            region = "None"

        try:
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        except:
            formatted_number = "None"
            
        print(f"""
    [+] Phone        : {phone_number}
    [+] Formatted    : {formatted_number}
    [+] Status       : {status}
    [+] Country Code : {country_code}
    [+] Country      : {country}
    [+] Region       : {region}
    [+] Timezone     : {timezone_info}
    [+] Tele Company : {operator}
    [+] Type Number  : {type_number}
    """)

    except:
        print("\n[ERROR] Invalid Format!")

except Exception as e:
    print(f"\n[ERROR] {str(e)}")
