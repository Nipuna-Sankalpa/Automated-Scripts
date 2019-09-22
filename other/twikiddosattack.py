import requests

url = "https://twiki.orangehrm.com/bin/rdiff/TWiki/TWikiScripts"
# /bin/rdiff/TWiki/WebStatistics
parameter = {
    'rev1': 14,
    'rev2': 13, 'sortcol': 0, 'table': 15, 'up': 0, 'sortcol': 1, 'table': 58, 'up': 0, 'sortcol': 2, 'table': 35,
    'up': 0, 'sortcol': 0, 'table': 93, 'up': 0, 'sortcol': 1, 'table': 90, 'up': 0
}

while True:
    print(requests.get(url, parameter))
    # time.sleep(2)
    print('Nipun')
