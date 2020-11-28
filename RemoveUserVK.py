import requests

access_token='YOUR_ACCESS_TOKEN'
def removeUsers(user_id):
    main_url = 'https://api.vk.com/method/groups.removeUser'
    response = requests.get(main_url, params={
        'group_id': 114689011,
        'user_id': user_id,
        'v' : 5.93,
        'access_token' : access_token,
    }).json()
    print (response)
rip = [
    USER_ID, USER_ID, USER_ID]
for i in range (0, len(rip)):
    removeUsers(rip[i])