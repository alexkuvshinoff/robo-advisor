# The robo-advisor project

# Description: 
# the robo advisor allows users to input a stock ticker to discover the latest closing price, recent high, and recent low of that stock

# in addition, the robo advisor gives a suggestion to the investor whether to buy or sell based on the following formula: If the stock's latest closing price is less than 20% above its recent low, "Buy", else "Don't Buy".

# Prerequisits:
    # Anaconda 3.7
    # Python 3.7
    # pip

# Installation
    # command line set up
        #cd robo-advisor
    # set up env
        # conda create -n stocks-env python=3.7 (first time only)
        # conda activate stocks-env
    # pip install
        # -r requirements.txt
# Set up
    # Before using or developing this application, take a moment to obtain an AlphaVantage API Key (e.g. "abc123").

    # After obtaining an API Key, create a new ".env" (in your local repo, NOT your remote repo), and update the contents of the ".env" file to specify your real API Key: ALPHAVANTAGE_API_KEY="abc123"

    # API KEY from: https://www.alphavantage.co/documentation/   

    # set up data and git ignore files

# Running the app
    # Run the recommendation script:
    # python app/robo_advisor.py
    # input a stock ticker into the program
