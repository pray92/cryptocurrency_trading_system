import requests

# 정책 변경으로 인한 Slacker 사용 불가
# Reference : https://developerdk.tistory.com/96
# Not_authed : https://pythonq.com/so/json/733487

def post_message(token, channel, text):
	response = requests.post("https://slack.com/api/chat.postMessage",
							headers={"Authorization": "Bearer " + token},
							data={"channel": channel, "text": text})
	print(response)

if __name__ == '__main__':
	token = ''
	channel = '#cryptocurrency'
	post_message(token, channel, "Heello")