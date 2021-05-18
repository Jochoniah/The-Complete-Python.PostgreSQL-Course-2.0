# numbers = [1,3,5]
# doubled =[x * 2 for x in numbers]
# print(doubled)

friends =[ "Rolf", "Sam", "Samatha", "Saurabh", "Jen"]
starts_s =[friend for friend in friends if friend.startswith("S")]
print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s:", id(starts_s))


# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

# print(starts_s)