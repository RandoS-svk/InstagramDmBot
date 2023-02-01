import instaloader
import pwinput

def GetUsers(username, password):
    instagram_data = instaloader.Instaloader()
    # Login or load session

    limit_users = 100
    limit_users_correct = False
    is_logged_in = False
    while limit_users_correct == False:
        try: 
            limit_users = 100
        except:
            limit_users = 100
        else:
            limit_users_correct = True

    while is_logged_in == False:
        try:
            login_info = instagram_data.login(username, password)        # (login)
        except:
            print('Bad password try it again')
            username = input('Enter Username: ')
            password = input('Instagram password: ')
        else:
            is_logged_in = True
            print('you are logged in')
            target_profile = input('Enter targeted profile: ')

    profile = instaloader.Profile.from_username(instagram_data.context, target_profile)
    follow_list = []
    count=0

    file = open("usernames.txt", "w")
    file.close()
    for follower in profile.get_followers():
        follow_list.append(follower.username)    
        file = open("usernames.txt","a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        count = count + 1
        if count == limit_users:
            break


