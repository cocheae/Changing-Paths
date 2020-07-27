# from firebase import firebase
#
# db = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/')
#
# 
#
# def slash_splitter(str_to_split):
#     class_number = str_to_split[-3] + str_to_split[-2] + str_to_split[-1]
#     list = []
#     for i in range(3):
#         str_to_split = str_to_split.replace(str_to_split[-1], '', 1)
#
#     for i in range((str_to_split.count('/') + 1)):
#         list.append(str_to_split.split('/')[i] + str(class_number))
#     return list
#
#
#
# def post_db(name_of_major, name_of_list):
#     for i in name_of_list:
#         db.post('/scrap/{} (Major)'.format(name_of_major), i)
#
#
# def maj_num(name_of_major, list_of_num):
#     return [name_of_major + ' ' + str(i) for i in list_of_num]
#
#
#
# l2, l3 = [], []
#
# start = ""
#
# while "stop" != start:
#     start = input("Enter Class String: ")
#     if start != "stop":
#         print(start)
#         l3.append(start)
#     else:
#         continue
#
#
# l3 = [i.split(':')[0] for i in l3]
#
# for i in l3:
#     l2 += slash_splitter(i)
#
#
# post_db(input("Enter Name of Major: "), l2)
#
#
#
#
#
#
#
# def take_input():
#     list = []
#     start = ""
#     while start != "stop":
#         start = input("")
#         if start != "stop":
#             list.append(start)
#         else:
#             continue
#     return list
