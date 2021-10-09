import socket
import json
import yaml

web_services_previous_ip = {"drive.google.com": '', "mail.google.com": '', "google.com": ''}
# ???????? ?????? ? ????????? ????????
with open("data_file.json", "w") as json_file:
    json.dump(web_services_previous_ip, json_file)
with open("data_file.yml", "w") as yaml_file:
    json.dump(web_services_previous_ip, yaml_file)

count = 1
while count < 3:
    for url in web_services_previous_ip.keys():
        ip = socket.gethostbyname(url)
        ip_old = web_services_previous_ip[url]

        if ip_old != '' and ip != ip_old:
            print('[ERROR] <', url, '> IP mismatch:', '<', ip, '>')
        else:
            print(url, ip)

        web_services_previous_ip[url] = ip
        with open("data_file.json", "w") as file:
            json.dump(web_services_previous_ip, file)
        with open("data_file.yml", "w") as yaml_file:
            yaml.dump(web_services_previous_ip, yaml_file)

    count += 1
