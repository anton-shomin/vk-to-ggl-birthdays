import json
import vk_api
# update date_of_birth getting
# Authenticate with VK API
LOGIN = input("Please enter your VK login \n")
PSSWD = input("Please enter your VK password \n")
vk_session = vk_api.VkApi(LOGIN, PSSWD)
vk_session.auth()

def date_of_birth_update(bdate):
    d = bdate.split('.')
    day, month = d[0], d[1]
    date_of_birth = ''
    if len(day) < 2:
        day = f'0{day}'
    if len(month) < 2:
        month = f'0{month}'
    date_of_birth = f'{day}-{month}'
    return date_of_birth

# get the VK API object
vk = vk_session.get_api()

# make the API request to get your friends with birthdate information
friend_info = vk.friends.get(fields='bdate')

# create a list to store the friend information
friend_list = []

# iterate through the friend information and add it to the list
for friend in friend_info['items']:
    if 'bdate' in friend:
        #first_name = friend.get('first_name', '').encode('utf-8').decode('utf-8')
        #last_name = friend.get('last_name', '').encode('utf-8').decode('utf-8')
        name = friend.get('first_name', '').encode('utf-8').decode('utf-8') + " " + friend.get('last_name', '').encode('utf-8').decode('utf-8')
        bdate = friend.get('bdate', '')
        
        if bdate:
            #date_of_birth = date_of_birth_update(bdate)
            friend_dict = {
                'name': name,
                'bdate': date_of_birth_update(bdate),
            }
            friend_list.append(friend_dict)

# write the friend information to a JSON file
with open('friend_info.json', 'w', encoding='utf-8') as f:
    json.dump(friend_list, f, ensure_ascii=False)

# print a message indicating the number of friends with birthdate information
print(f'Found {len(friend_list)} friends with birthdate information.')
