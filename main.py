# Version 0

from consolemenu import *
from consolemenu.screen import *
from consolemenu.items import *
from consolemenu.format import *
from configparser import ConfigParser, MissingSectionHeaderError
import requests
import time
import os

try:
    config = ConfigParser()
    config.read("instaosint.config")
    sessionid = config["CREDS"]["sessionid"]
    csrf = config["CREDS"]["csrftoken"]
    session = requests.Session()
    cookies_jar = requests.cookies.RequestsCookieJar()
    cookies_jar.set('sessionid', sessionid)
    session.cookies = cookies_jar
    session.headers = {
        'x-instagram-ajax': '4f336da7de59',
        'x-csrftoken': csrf,
        'x-ig-app-id': '936619743392459'
    }
    base = "https://www.instagram.com"
    src = session.post(f"{base}/instagram?__a=1")
    graphql = src.json()['graphql']['user']
except KeyError:
    print("I fucking hate you.")
    Screen.printf("There is an error with your config, please visit Config Manager.")
except MissingSectionHeaderError:
    print("Get fucked truly")
    Screen.printf("There is an error with your config, please visit Config Manager.")
except ValueError:
    print("eatitlikeit\'sdevil\'scunt")
    Screen.printf("!ꜝ Instagram did not accept your auth info, please visit Config Manager. ꜝ!")

def accountCheck():
    # x = input()
    print("Please turn every instance of % to %% on input")
    if os.path.isfile("instaosint.config") == True:
        print("Config file already exists, checking if the credentials still work.")
        try:
            if src.json()['graphql']['user']['id'] == "25025320":
                print("Config works!")
            else:
                print("What the fuck!")
        except ValueError:
            print("Config does not work. Issue: Invalid credentials!")
            print("Enter your sessionid cookie.\n")
            sessionid = input()
            print("Enter your csrftoken cookie.\n")
            csrftoken = input()
            config_object = ConfigParser()
            config_object["CREDS"] = {
                "sessionid": sessionid,
                "csrftoken": csrftoken
            }
            with open('instaosint.config', 'w+') as conf:
                config_object.write(conf)
            print("Reconfiguration done! Please restart the code!")
            exit()
        except KeyError:
            print("Config does not work. Issue: File empty or invalid input, fixing config.")
            print("Enter your sessionid cookie.\n")
            sessionid = input()
            print("Enter your csrftoken cookie.\n")
            csrftoken = input()
            config_object = ConfigParser()
            config_object["CREDS"] = {
                "sessionid": sessionid,
                "csrftoken": csrftoken
            }
            with open('instaosint.config', 'w+') as conf:
                config_object.write(conf)
            print("Reconfiguration done! Please restart the code!")
            exit()
        except NameError:
            print("Config does not work. Issue: File empty or invalid input, fixing config.")
            print("Enter your sessionid cookie.\n")
            sessionid = input()
            print("Enter your csrftoken cookie.\n")
            csrftoken = input()
            config_object = ConfigParser()
            config_object["CREDS"] = {
                "sessionid": sessionid,
                "csrftoken": csrftoken
            }
            with open('instaosint.config', 'w+') as conf:
                config_object.write(conf)
            print("Reconfiguration done! Please restart the code!")
            exit()
    else:
        print("Config does not exist! Creating one for you.")
        print("Enter your sessionid cookie.\n")
        sessionid = input()
        print("Enter your csrftoken cookie.\n")
        csrftoken = input()
        config_object = ConfigParser()
        config_object["CREDS"] = {
            "sessionid": sessionid,
            "csrftoken": csrftoken
        }
        with open('instaosint.config', 'w+') as conf:
            config_object.write(conf)
        print("Configuration done! Please restart the code!")
        exit()
    time.sleep(5)
def getUser(username):
        src = session.post(f"{base}/{username}?__a=1")
        graphql = src.json()['graphql']['user']
        
        if "🏳️‍🌈" in graphql['biography'] or "🏳️‍🌈" in graphql['full_name']:
            isGayBool = True
        else:
            isGayBool = False

        responseDict = {
            "userId": graphql["id"],
            "fullName": graphql["full_name"],
            "bio": graphql["biography"],
            "profilePicUrl": graphql["profile_pic_url_hd"],
            "site": graphql["external_url"],
            "followerAmount": graphql["edge_followed_by"]["count"],
            "followAmount": graphql["edge_follow"]["count"],
            "followsYou": graphql["follows_viewer"],
            "followedByYou": graphql["followed_by_viewer"],
            "blockedByYou": graphql["blocked_by_viewer"],
            "restrictedByYou": graphql["restricted_by_viewer"],
            "isPrivate": graphql["is_private"],
            "isVerified": graphql["is_verified"],
            "isJoinedRecently": graphql["is_joined_recently"],
            "isGay": isGayBool
        }
        return responseDict
def userToFile():
    print("Enter Username\n")
    username = input()
    user_data = getUser(username)
    user_data_file = open(f"{username}.txt", "a+", encoding="utf-8")
    try:
        user_data_file.write(f"User ID: {user_data['userId']}\n")
    except KeyError:
        print("Problem getting/writing: User ID")

    try:
        user_data_file.write(f"Full Name: {user_data['fullName']}\n")
    except KeyError:
        print("Problem getting/writing: Full Name")

    try:
        user_data_file.write(f"Bio: {user_data['bio']}\n")
    except KeyError:
        print("Problem getting/writing: Bio")

    try:
        user_data_file.write(f"Profile Picture URL: {user_data['profilePicUrl']}\n")
    except KeyError:
        print("Problem getting/writing: Profile Picture URL")

    try:
        user_data_file.write(f"Site: {user_data['external_url']}\n")
    except KeyError:
        print("Problem getting/writing: User Bio Link")

    try:
        user_data_file.write(f"Follower Count: {user_data['followerAmount']}\n")
    except KeyError:
        print("Problem getting/writing: Follower Count")

    try:
        user_data_file.write(f"Following Count: {user_data['followAmount']}\n")
    except KeyError:
        print("Problem getting/writing: Following Count")

    try:
        user_data_file.write(f"Follows You: {user_data['followsYou']}\n")
    except KeyError:
        print("Problem getting/writing: Follows You Status")

    try:
        user_data_file.write(f"You Follow: {user_data['followedByYou']}\n")
    except KeyError:
        print("Problem getting/writing: Followed By You Status")
    
    try:
        user_data_file.write(f"You Blocked: {user_data['blockedByYou']}\n")
    except KeyError:
        print("Problem getting/writing: \"You Blocked\" Status")

    try:
        user_data_file.write(f"You Restricted: {user_data['restrictedByYou']}\n")
    except KeyError:
        print("Problem getting/writing: \"You Restricted\" Status")

    try:
        user_data_file.write(f"Is User Private: {user_data['isPrivate']}\n")
    except KeyError:
        print("Problem getting/writing: \"Account Private/Public\" Status")

    try:
        user_data_file.write(f"Is User Verified: {user_data['isVerified']}\n")
    except KeyError:
        print("Problem getting/writing: Verified Status")

    try:
        user_data_file.write(f"Is User Recently Joined: {user_data['isJoinedRecently']}\n")
    except KeyError:
        print("Problem getting/writing: Recently Joined Status")

    try:
        user_data_file.write(f"Is User Gay: {user_data['isGay']}\n")
    except KeyError:
        print("Problem getting/writing: Is Gay Status")
    
        # user_data_file.write(
        #     f"""
        #     User ID: {user_data["userId"]}
        #     Full Name: {user_data["fullName"]}
        #     Bio: {user_data["bio"]}
        #     Profile Picture URL: {user_data["profilePicUrl"]}
        #     Site: {user_data["external_url"]}
        #     Follower Count: {user_data["followerAmount"]}
        #     Following Count: {user_data["followAmount"]}
        #     Follows You: {user_data["followsYou"]}
        #     You Follow: {user_data["followedByYou"]}
        #     You Blocked: {user_data["blockedByYou"]}
        #     You Restricted: {user_data["restrictedByYou"]}
        #     Is User Private: {user_data["isPrivate"]}
        #     Is User Verified: {user_data["isVerified"]}
        #     Is User Recently Joined: {user_data["isJoinedRecently"]}
        #     Is User Gay: {user_data["isGay"]}
        #     """
        # )
def usernameToId():
        print("Enter Username:\n")
        username = input
        src = session.post(f"{base}/{username}?__a=1")
        graphql = src.json()['graphql']['user']['id']
        print(graphql)
menu = ConsoleMenu("InstaOSINT", "Tool by dirt3009")

configManager_item = FunctionItem("Config Manager", accountCheck)
userIdResolver_item = FunctionItem("Username -> User ID", usernameToId)
infoSaver_item = FunctionItem("Save User Info", userToFile)

menu.append_item(configManager_item)
menu.append_item(userIdResolver_item)
menu.append_item(infoSaver_item)

menu.show()
