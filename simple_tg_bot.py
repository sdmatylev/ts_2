import requests


def send_message(text):
    token = "5443577063:AAFOL80ymXGGzP-VazlRt6OslcQ1ktPS9zI"
    chat_id = "932219977"
    url_request = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_request)
    print(results.json())
