import requests
import json
import datetime, time

method = 'users.get'
serviceAccessKey = '41c074a841c074a841c074a88b41af849c441c041c074a81f970c0a33271ec8b480b3aa'
fields = 'online, last_seen'
APIVersion = 5.103

try:
    userID = int(input())

    url = 'https://api.vk.com/method/{}?user_ids={}&fields={}&access_token={}&v={}'.format(method, userID, fields,
                                                                                           serviceAccessKey, APIVersion)
    try:
        result = json.loads(requests.get(url).text)
        if 'error' in result.keys():
            print(result['error']['error_msg'])
        elif len(result['response']) == 0:
            print("Invalid UserID.")
            exit(1)
        else:
            result = result['response'][0]
            if result['online'] == 1:
                print('0:00:00')
            else:
                try:
                    lastSeenTime = result['last_seen']['time']
                    lastSeenTime = datetime.datetime.fromtimestamp(lastSeenTime)
                    dt = datetime.datetime.now()
                    currentTime = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
                    print(currentTime - lastSeenTime)
                except KeyError as k:
                    print("Profile with this ID has been deleted, or not created yet.")
                    exit(1)
    except requests.exceptions.ConnectionError as e:
        print('Connection Error.')
except ValueError as e:
    print("Invalid UserID.")
    exit(1)
