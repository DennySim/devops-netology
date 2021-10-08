# import os
#
# repo_dir = "e:\\netology\\devops\\devops-netology\\"
# bash_command = ["cd " + repo_dir, "git status"]
# result_os = os.popen(' && '.join(bash_command)).read()
# print()  # add empty line
# for result in result_os.split('\n'):
#     if result.find('modified') != -1:
#         prepare_result = result.replace('\tmodified:   ', '').replace('/', '\\')
#         print('File pathname ', repo_dir, prepare_result, sep='')



# import os
# default_repo_dir = "e:\\netology\\devops\\devops-netology\\"
# repo_dir = input('Enter path to repo [default dir - ' + default_repo_dir + ']' ) or default_repo_dir
#
# bash_command = ["cd " + repo_dir, "git status"]
# result_os = os.popen(' && '.join(bash_command)).read()
# print()  # add empty line
# if os.path.isdir(repo_dir + ".git"):
#     print("THATS A GIT REPO!", '\n')
# else:
#     print("THIS IS NOT A GIT REPO!")
# for result in result_os.split('\n'):
#     if result.find('modified') != -1:
#         prepare_result = result.replace('\tmodified:   ', '').replace('/', '\\')
#         print('File pathname ', repo_dir, prepare_result, sep='')


# import socket
# web_services_previous_ip = {"drive.google.com": '', "mail.google.com": '', "google.com": ''}
# count = 1
# while count < 1000:
#     for url in web_services_previous_ip.keys():
#         ip = socket.gethostbyname(url)
#         ip_old = web_services_previous_ip[url]
#         if ip_old != '' and ip != ip_old:
#             print('[ERROR] <', url, '> IP mismatch:', '<', ip, '>')
#             web_services_previous_ip[url] = ip
#         else:
#             print(url, ip)
#     count += 1
