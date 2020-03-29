import ssl
import os
import slack

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
client = slack.WebClient(token='<your web token>', ssl=ssl_context)

def main():
    response = client.chat_postMessage(
        channel='<channel id>',
        text="Hello world!")

    if response["type"] == "url_verification":
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        response_data = {
            "challenge":message.get('challenge')
        }

    assert response["ok"]
    assert response["message"]["text"] == "Hello world!"

if __name__ == "__main__":
    main()

