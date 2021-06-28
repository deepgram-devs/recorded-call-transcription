# flask (server)
import flask
from flask import (Flask, request)

# twilio helper library
from twilio.rest import Client  # type: ignore

# other imports
import time
import requests
import json
import os
import uuid

from dotenv import load_dotenv  # type: ignore

load_dotenv()  # take environment variables from .env.

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
DEEPGRAM_API_KEY = os.environ['DEEPGRAM_API_KEY']

app = Flask(__name__, static_url_path="/static/", static_folder="static")


@app.route('/')
def index() -> flask.Response:
    return app.send_static_file('index.html')


def get_twilio(url: str) -> requests.Response:
    return requests.get(url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))


@app.route('/start-call/', methods=['POST'])
def start_call() -> dict:
    body = json.loads(request.data)
    # our account sid and auth token from twilio.com/console
    # the twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # make the outgoing call
    call = client.calls.create(
        twiml='<Response><Record /></Response>',
        to=body['to_number'],
        from_=body['from_number']
    )
    # get the call sid of the outgoing call
    sid = call.sid
    # get the url where we can retrieve info about the call recording
    call_url = "https://api.twilio.com/2010-04-01/Accounts/" + \
        TWILIO_ACCOUNT_SID + "/Calls/" + sid + ".json"
    call_req = get_twilio(call_url)
    recording_sub_url = call_req.json()['subresource_uris']['recordings']

    return {"recording_sub_url": recording_sub_url}


@app.route('/get-recording/', methods=['POST'])
def poll_recording() -> dict:
    body = json.loads(request.data)
    print("got request in poll_recording:", body)
    recording_sub_url = body["recording_sub_url"]
    call_recording_url = "https://api.twilio.com" + recording_sub_url
    call_recording_req = get_twilio(call_recording_url)
    recordings = call_recording_req.json()['recordings']
    # check if a (the) recording is available
    if len(recordings) == 0:
        return {"status": "CALL_NOT_STARTED"}
    else:
        recording_url = "https://api.twilio.com" + recordings[0]['uri']
        recording_req = get_twilio(recording_url)
        # check if the recording is completed
        if recording_req.json()['status'] != 'completed':
            return {"status": "CALL_STARTED"}
        else:
            recording_complete = True
            audio_url = os.path.splitext(recording_url)[0] + '.wav'
            return {"status": "CALL_ENDED", "audio_url": audio_url}


@app.route('/transcribe/', methods=['POST'])
def transcribe() -> dict:
    body = json.loads(request.data)
    print("got request in transcribe:", body)
    print('sending recording to deepgram')
    # submit the recording to deepgram
    deepgram_req = requests.post(
        'https://brain.deepgram.com/v2/listen?punctuate=true',
        headers={"Authorization": "token" + DEEPGRAM_API_KEY},
        json={"url": body["audio_url"]}
    )
    print('done processing request, sending deepgram response back to client',
          deepgram_req.text)
    return json.loads(deepgram_req.text)
