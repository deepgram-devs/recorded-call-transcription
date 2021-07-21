# Transcribing Recorded Calls using Deepgram

[![Remix on Glitch](https://img.shields.io/badge/Glitch-remix-blue?logo=glitch)](#remix-on-glitch)

The wealth of knowledge in the conversations that happen during your sales and
support calls can be left untapped without automatic transcription. This app
aims to demonstrate how to use Deepgram API to transcribe a phone call recorded
through [Twilio](https://www.twilio.com/).

## Prerequisites

You will need:

- A [free Deepgram account](https://console.deepgram.com/signup?utm_source=DEVREL&utm_medium=github&utm_content=recorded-call-transcription)
- A Deepgram [API key](https://developers.deepgram.com/getting-started/create-api-key)
- A [Twilio account](https://twilio.com)
- A Twilio Account SID & Auth Token

## Getting started

You can run this application by remixing it on Glitch or by running it on your
local computer.

### Remix on Glitch

Glitch comes with an online editor, so you'll have all the necessary tools
to explore your own app instance. Actions taken in Glitch are subject to [Glitch’s Terms of Service and Privacy Policy](https://glitch.com/legal) and are not covered by any Deepgram agreements.

To remix this application on Glitch, go to the following URL:

> https://glitch.com/edit/#!/remix/dg-uc-recorded-call-transcription

When accessing this URL in your browser, the project will be forked and deployed.

#### Configure the settings

Your application will need to know more about you before it can run successfully. Edit the environment variables (`.env`) to reflect the settings you want to use:

- `YOUR_TWILIO_ACCOUNT_SID`: The Account SID from your Twilio Account Dashboard.
- `YOUR_TWILIO_AUTH_TOKEN`: The Auth Token from your Twilio Account Dashboard.
- `DG_KEY`: The API Key you created earlier in this tutorial.

Once these variables are set, the application should run automatically.

### Run on localhost

To run this project on your local computer:

#### Clone the repository

Either clone or download the repository to your local machine in a new directory:

```bash
# Clone this repo
git clone https://github.com/deepgram-devs/recorded-call-transcription.git

# Move to the created directory
cd recorded-call-transcription
```

#### Configure the settings

Your application will need to know more about you before it can run. Copy the
`.env-example` file into a new file named `.env`, and edit the new file to
reflect the settings you want to use:

- `YOUR_TWILIO_ACCOUNT_SID`: The Account SID from your Twilio Account Dashboard
- `YOUR_TWILIO_AUTH_TOKEN`: The Auth Token from your Twilio Account Dashboard
- `DG_KEY`: The Deepgram API key you created earlier in this tutorial.

#### Create a virtual environment (optional)

Create a virtual Python environment to run the server in isolation 
and prevent version collisions with other projects. (You can skip this part if you don't mind installing things system-wide.)

```bash
# Create the virtual environment
# (Must be run only once.)
python3 -m venv dg-twilio-ve

# Activate the virtual environment
# (Must be run every time you open a new terminal.)
source dg-twilio-ve/bin/activate
# Your prompt should start with `(dg-twilio-ve)`.

# python3 and pip3 will now run in this virtual environment.
# If you want to deactivate this environment, type `deactivate`.
```

#### Install the dependencies

In the directory where you downloaded the code, run the following command to
bring in the dependencies needed for this project:

```bash
pip3 install -r requirements.txt
```

#### Start the server

Now that you have configured your application and put the dependencies in place, your application
is ready to go! Run it with:

```bash
FLASK_APP=server.py FLASK_ENV=development flask run
```

## Development and contributing

Interested in contributing? We ❤️ pull requests!

To make sure our community is safe for all, be sure to review and agree to our
[Code of Conduct](./CODE_OF_CONDUCT.md). Then see the
[Contribution](./CONTRIBUTING.md) guidelines for more information.

## Getting help

We love to hear from you, so if you have questions or comments, or find a bug in the
project, let us know! You can either:

- [Open an issue](https://github.com/deepgram-devs/recorded-call-transcription/issues/new) on this repository
- Tweet at us! We're [@DeepgramDevs on Twitter](https://twitter.com/DeepgramDevs)

## Further reading

Check out the Developer Documentation at [https://developers.deepgram.com/](https://developers.deepgram.com/).
