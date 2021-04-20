# What is this app for?

This app aims to demonstrate how to use Deepgram API to transcribe
a phone call recorded through [Twilio](https://www.twilio.com/).

**WARNING**: This is an example application only designed for demoing. We
strongly discourage direct use of this code in production environnement.

# How can I deploy it?

_Prerequisites: Deepgram account and API Key, Twilio account SID & Auth Token._

You can "remix" this application on Glitch. In the following URL, replace:

1.  `INSERT_DG_KEY_HERE` and `INSERT_DG_SECRET_HERE` with Deepgram API key and secret,
2.  `INSERT_TWILIO_ACCOUNT_SID_HERE` and `INSERT_TWILIO_AUTH_TOKEN_HERE` with Twilio data.

> https://glitch.com/edit/#!/remix/dg-talk-time-analytics?DG_KEY=INSERT_DG_KEY_HERE&DG_SECRET=INSERT_DG_SECRET_HERE&TWILIO_ACCOUNT_SID=INSERT_TWILIO_ACCOUNT_SID_HERE&TWILIO_AUTH_TOKEN=INSERT_TWILIO_AUTH_TOKEN_HERE

When accessing this URL in your browser, the project will be forked and deployed. Glitch comes with
an online editor so you'll have all the needed tools to play with your own app instance!

# Can I run it on my own computer?

_Prerequisites: Deepgram account and API Key, Twilio account SID & Auth Token._

Yes, of course! First, copy-paste those lines in your terminal:

```bash
# Clone this repo
git clone https://github.com/deepgram/recorded-call-transcription.git
# move to the created directory
cd recorded-call-transcription
```

In the following snippet, replace:

1. `INSERT_DG_KEY_HERE` and `INSERT_DG_SECRET_HERE` with your Deepgram API key and secret,
2. `INSERT_TWILIO_ACCOUNT_SID_HERE` and `INSERT_TWILIO_AUTH_TOKEN_HERE` with Twilio data.

Then save this snippet as a file named `.env`
(note that this is bash-like file, so spaces around `=` are not allowed).

```bash
DG_KEY=INSERT_KEY_HERE
DG_SECRET=INSERT_SECRET_HERE
TWILIO_ACCOUNT_SID=INSERT_TWILIO_ACCOUNT_SID_HERE
TWILIO_AUTH_TOKEN=INSERT_TWILIO_AUTH_TOKEN_HERE
```

Then, create a virtual python environnement to run the server in an isolated environnement
and prevent version collisions with other projects
(you can skip this part if you don't mind installing things "system-wide").

```bash
# create the virtual environnement
# (has to be run only once)
python3 -m venv dg-twilio-ve
# activate the virtual envrionnement
# (has to be run every time you open a new terminal)
source dg-twilio-ve/bin/activate
# your prompt should start with `(dg-twilio-ve)`.
# Now python3 and pip3 will run in this virtual environnement.
# If you want to deactivate this env, just type `deactivate`.
```

Finally, install the dependencies and start the server:

```bash
pip3 install -r requirements.txt
FLASK_APP=server.py FLASK_ENV=development flask run
```

# How does it work?

The server mainly acts as a proxy between the browser on the one hand
and on other hand Deepgram and Twilio APIs (this proxy step hides the
Deepgram and Twilio credentials to the user). Here is the workflow:

1. User requests `/` to the server and gets the `index.html` file as
   a response.
2. The user fill in the two phone numbers, clicks on "Call".
3. An AJAX request is sent to the server (see the `/start-call/` endpoint
   in `server.py`). In turn, the server will
   trigger a Twilio call and send back an URL to be polled to get the recording.
4. Every second, the browser will send a request to the `/get-recording/`. This
   endpoint will request the Twilio API to get the call recording. Depending on
   the call status, the `/get-recording` endpoint can answer `CALL_NOT_STARTED`,
   `CALL_STARTED`, `CALL_ENDED`. The browser use those status to update the
   button label ("Calling...", "Call in progress...", "Transcribe in progress...").
5. In case of `CALL_ENDED`, the `/get-recording/` endpoint also adds an
   `audio_url` field in the response.
   The browser will then request the `/transcribe/`
   endpoint with this `audio_url`. In turn, the `/transcribe/` endpoint will
   forward this `audio_url` to Deepgram API and send back the transcript to the
   user.
6. When the browser finally get the transcript, it hides the form and display it.

# Notes on CSS

The `static/main.css` is a CSS file generated with [Tailwindcss](https://tailwindcss.com/).
For development convenience, we ship the raw output with all classes in it.
For an actual application, you would certainly like to
["purge" this file](https://tailwindcss.com/docs/optimizing-for-production#writing-purgeable-html).
