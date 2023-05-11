import json
import vk_api

# Authenticate with VK API
LOGIN = input("Please enter your VK login \n")
PSSWD = input("Please enter your VK password \n")
vk_session = vk_api.VkApi(LOGIN, PSSWD)
vk_session.auth()

# get the VK API object
vk = vk_session.get_api()

# make the API request to get your friends with birthdate information
friend_info = vk.friends.get(fields='bdate')

# create a list to store the friend information
friend_list = []

# iterate through the friend information and add it to the list
for friend in friend_info['items']:
    if 'bdate' in friend:
        first_name = friend.get('first_name', '').encode('utf-8').decode('utf-8')
        last_name = friend.get('last_name', '').encode('utf-8').decode('utf-8')
        name = first_name + " " + last_name
        bdate = friend.get('bdate', '')

        if bdate:
            date_of_birth = ''
            if len(bdate.split('.')) == 3:
                day, month, year = bdate.split('.')
                if len(day) < 2:
                    day = f'0{day}'
                if len(month) < 2:
                    month = f'0{month}'

                date_of_birth = f'{day}-{month}'
            else:
                day, month = bdate.split('.')
                if len(day) < 2:
                    day = f'0{day}'
                if len(month) < 2:
                    month = f'0{month}'
                date_of_birth = f'{day}-{month}'

            friend_dict = {
                'name': name,
                'bdate': date_of_birth,
            }
        friend_list.append(friend_dict)

# write the friend information to a JSON file
with open('friend_info.json', 'w', encoding='utf-8') as f:
    json.dump(friend_list, f, ensure_ascii=False)

# print a message indicating the number of friends with birthdate information
print(f'Found {len(friend_list)} friends with birthdate information.')
