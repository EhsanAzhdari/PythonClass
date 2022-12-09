import instaloader
import getpass


f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line.strip())
f.close()

L = instaloader.Instaloader()

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

L.login(username, password)
print("Hooora!!! Successfully Logged in!")

profile = instaloader.Profile.from_username(L.context, "sajjad_aemmi")

#Create a List OF Now Follower
new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

#Unfollow print
for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)

#Instagram New Follower Finder --> (Create A List OF Just New Followers)
new_followers_finder = []
for new_follower in new_followers:
    if new_follower not in old_followers:
        new_followers_finder.append(new_follower)

#Write New Follower in a File
f = open("instagram new followers finder.txt", "w")
for follower in new_followers_finder:
    f.write(follower + "\n")
f.close()

#Write Now Follower in a File
f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()

