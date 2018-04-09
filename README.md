# LyricBot
Scrapes Genius for lyrics, then uses those lyrics as a model for a character-based recurrent neural network.

Based off of https://github.com/johnwmillr/LyricsGenius and https://github.com/sherjilozair/char-rnn-tensorflow: this project is built off the shoulders of their great work.

# Requirements
Requires Python 3.6 with TensorFlow, Twython, beautifulsoup4, and requests. You will also need API keys for both Genius and Twitter: guides on how to get both of these as well as how to install the above dependencies can be found online. This currently uses PowerShell to automate the passing of arguments to .py files; and any PC that can run TF should have PowerShell anyways. Still, in the future I may remove the PowerShell dependency since I acknowledge that it is a clunky implementation.

# Setup
After cloning this repository, you should open credentials.ini and add the relevant Genius API credentials (client_id, client_secret, and client_access_token). The same should be done in twitter_access.py: APP_KEY, APP_SECRET, OAUTH_TOKEN, and OAUTH_TOKEN_SECRET should be appropriately assigned. This is a one-time setup: however if the values are somehow wrong then this may behave in unexpected manners.

# Use
Open the .ps1 file using PowerShell and enter the name of an artist whose lyrics you'd like to use as a model. Depending on the size of their body of work, it can take anywhere from 5 minutes to an hour to scrape Genius and crunch the data.

# Disclaimer
I am not a data scientist. This project isn't serious: it was a fun way to put together a few of my passions, and taught me a lot about programming in general. In no way will the output be intelligible; but it makes it very easy to throw together a novelty Twitter bot.
