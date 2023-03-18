import DoomerBot
import os
from dotenv import load_dotenv, find_dotenv

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    print(os.getenv("TOKEN"))
    DoomerBot.run_bot()