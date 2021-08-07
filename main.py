import json

import keys
import message_to_slack as slk

if __name__ == '__main__':
	# 1. json에서 키 값을 가져와 초기화

	# keys.json
	with open('keys.json', 'r') as f:
		json_data = json.load(f)

	# json 기반으로 전역 변수를 초기화합니다.
	# 업비트 Key
	keys.UPBIT_ACCESS_KEY = json_data['access']
	keys.UPBIT_SECRET_KEY = json_data['secret']

	# 슬랙 토큰 및 채널
	if 'slack' in json_data.keys():
		keys.SLACK_TOKEN = json_data['slack']['token']
		keys.SLACK_CHANNEL = json_data['slack']['channel']

	# 전역 변수 기반 메시지 보내기
	slk.post_message(keys.SLACK_TOKEN, keys.SLACK_CHANNEL, '안녕하세요! 주인님')
