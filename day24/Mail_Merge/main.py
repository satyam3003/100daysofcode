with open('day24/Mail_Merge/Input/Letters/starting_letter.txt') as file:
    content = file.read()
    content = content.strip()
    print(content)

with open('day24/Mail_Merge/Input/Names/invited_names.txt') as names:
    all_names = names.read()
    all_names = all_names.split("\n")
    # print(all_names)

for name in all_names:
    send_list = content.replace('[name]', name)
    send_list = send_list.replace('Angela', 'Satyam')
    location_address = f"day24/Mail_Merge/Output/ReadyToSend/{name}.txt"
    with open(location_address, mode='w') as sendfile:
        sendfile.write(send_list)


