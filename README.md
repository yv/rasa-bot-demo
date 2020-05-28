# Simple RASA Demo
This repository aims to demonstrate how you can progress further from the
simple RASA moodbot (the result of `rasa init`) to something that's
actually useful in some sense.

For security reasons, it is not advisable to expose a RASA server or the
action server to the open internet. This should help you to get started,
but it's not something you could or should use as a basis for a production
deployment of a RASA chatbot.

## Prerequisites
You will need Python 3.7 to get started. (Install via Homebrew or Anaconda).
Then, create the virtual environment and activate it with
```
python -m venv venv
source venv/bin/activate
```

Now you can install the required packages with
```
pip install -r requirements.txt
```

## Starting the Bot Demo
Start the action server with
```
rasa run action
```

In a different terminal, start the RASA server with
```
rasa run
```

And finally serve the web page with the RASA widget using
```
python -m SimpleHTTPServer
```
(Caution: this will run a HTTP server on port 8000 that is visible on the
local network. Do not do this in a public network.)

Finally, open your browser at http://localhost:8000 and you have
a simple RASA bot you can interact with.
