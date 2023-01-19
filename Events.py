import pip._vendor.requests 
import json
import pprint

def main():
    events = getEvents()

    # Verify first event
    pprint.pprint(events[0])
    print(f"Event Name: {events[0]['event_name']}")


def getEvents():
    url = 'https://courses.ianapplebaum.com/api/syllabus/1'
    headers = { 'Authorization': 'Bearer PU4UGN2sUPaEG1yw1CmOuyzX2DhhDeC2G6OLHn97',
            'Content-Type': 'application/json',
            'Accept': 'application/json' 
}
    r = pip._vendor.requests.get(url, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)

        return data['events']
    else:
        print(f"Error: {r.status_code}")

    

main()

