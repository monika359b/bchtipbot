import os


# Define settings
try:
    DEBUG = os.environ["DEBUG"] == "True"  # because DEBUG is a string
except KeyError:
    DEBUG = True


try:
    TOKEN = os.environ["TOKEN"]
except KeyError:
    # This Token is for the test bot.
    # It is recommended that you create your own bot for testing and create the
    # TOKEN environment variable.
    # I will still leave my test token here for quick testing.
    TOKEN = "5572020003:AAHJ8zcJjXkLd7hfd__sArmcg4s0XDKp2fw"


# Your output BCH address
FEE_ADDRESS = "ltc1qe4jw5dk0gpqckndsatg7glncz848mw7l30992s"
# The fee you want to charge (0.01 is 1%)
FEE_PERCENTAGE = 0.00


# List of administrators allowed to use the admin commands
ADMIN_LIST = [
    "Rohit_kumawat_1",
]
