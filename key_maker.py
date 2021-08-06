import json
from collections import OrderedDict

"""
업비트 계좌의 Open API Access/Secret Key
그리고 필요하다면 Slack의 토큰 키를 json에 저장합니다.
"""
def make_key_json(access_key :str, secret_key :str, token :str):
	json_data = OrderedDict()
	json_data['access'] = access_key
	json_data['secret'] = secret_key
	if token != '':
		json_data['token'] = token
	
	# Print json
	print(json.dumps(json_data, ensure_ascii=False, indent="\t"))

	with open('keys.json', 'w', encoding='utf-8') as make_file:
		print(json.dump(json_data, make_file, ensure_ascii=False, indent="\t"))


if __name__ == '__main__':
	access = input('Access Key : ')
	secret = input('Secret Key : ')
	token = input('Token for Slack(May ignore) : ')
	make_key_json(access, secret, token)