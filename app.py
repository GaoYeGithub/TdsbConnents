import requests
from datetime import datetime

def fetch_tdsb_timetable(school_id, date, auth_token):
    base_url = "https://zappsmaprd.tdsb.on.ca"
    endpoint = f"/api/TimeTable/GetTimeTable/Student/{school_id}/{date}/{date}"
    
    headers = {
        "X-Client-App-Info": "Python||2024Aug29|False|1.0.0|False|1|False)",
        "Authorization": f"Bearer {auth_token}"
    }
    
    response = requests.get(f"{base_url}{endpoint}", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

def format_date(date):
    return date.strftime("%d%m%Y")

if __name__ == "__main__":
    school_id = "1145"
    date = datetime(2024, 9, 3)
    auth_token = "YOUR_AUTH_TOKEN_HERE"
    
    formatted_date = format_date(date)
    timetable = fetch_tdsb_timetable(school_id, formatted_date, auth_token)
    
    print(f"Timetable for {date.strftime('%B %d, %Y')}:")
    print(timetable)