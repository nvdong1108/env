import requests

def get_holidays(year):
    url = f'https://date.nager.at/api/v3/publicholidays/2034/JP'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            holidays = response.json()
            dates = [holiday['date'] for holiday in holidays]
            return dates
        else:
            print(f'Failed to call API for year {year}. Status code: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Error calling API for year {year}: {e}')
        return None

holiday_dates = get_holidays(2024)
if holiday_dates:
    for date in holiday_dates:
        print(date)
