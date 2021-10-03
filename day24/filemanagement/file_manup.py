# ---------------- MODE 1 - reading a file -------------------
# file = open('day24/filemanagement/my_file.txt', mode='r')
# content = file.read()
# print(content)
# file.close()


# ---------------- MODE 2 - reading a file ----------------
# with open('day24/filemanagement/my_file.txt') as file:
#     content = file.read()
#     print(content)


# ------------------ Writing a file -------------------
# with open('day24/filemanagement/my_file.txt', mode='w') as file:  # w stand for write
#     file.write("This is my updated writeup")


# ------------------ Append to file dont delete the origial content just add to it ----------
# with open('day24/filemanagement/my_file.txt', mode='a') as file:  #a stand for append
#     file.write("\nThis is appended text")