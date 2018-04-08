import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import requests
import grequests

def main():
    payload = {"message":"Hi!"}
    urls = {
        "http://us-central1-happy-feet-200513.cloudfunctions.net/function-1"
        }

    button = aiy.voicehat.get_button()

    while True:
        button.wait_for_press()
        print('Button pressed!')
        rs = (grequests.post(u) for u in urls)
        grequests.map(rs)


main()