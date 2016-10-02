import vk
import requests
import getpass


APP_ID = 5648676


def get_user_login():
    print('Enter your VK login:')
    return input()


def get_user_password():
    print('Enter your VK password:')
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends = api.friends.getOnline()
    return api.users.get(user_ids=friends, fields=['first_name', 'last_name'])


def output_friends_to_console(friends_online):
    print('Your online friends:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
