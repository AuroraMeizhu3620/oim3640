import requests
# #GET: read all messages
# data = requests.get('https://oim.108122.xyz/messages').json()
# for msg in data:
#     print(msg)

# # POST: send a message(1-140 characters)
# requests.post('https://oim.108122.xyz/messages', 
#               json={'message':'good luck to all for course selections!'},
#               headers = {'X-Token': 'meizhumeizhu'})

# def delete_message():
#     data = requests.get('https://oim.108122.xyz/messages').json()
#     for msg in data:
#         if msg['message'] == 'good luck to all for course selections!':
#             id = msg['id']
#             requests.delete(f'https://oim.108122.xyz/messages/{id}', headers={'X-Token': 'meizhumeizhu'})

# delete_message()

