
from fastapi import FastAPI
import random

app = FastAPI()

# we will build two simple get endpoints
# side_hustles
# money_quotes

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell physical products without holding any inventory",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Promote products and earn commissions",
    "Crypto - Trading - Buy  and sell cryptocurrencies",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand -Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "Youtube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Manegement - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for bussinesses!", 
]

money_quotes = [
    "The was to get started is to quit talking and begin doing. Walk Disney",
    "Formal education will make you a living; self-education will make you a fortune. Jim Rohn",
    "If you don't find a way to make money while you sleep, you will work until you die.",
    "Do not save what is left after spending; spend what is left after saving. Warren Buffett",
    "Money terrible master but an excellent servant. P.T. Barnum ",
    "You must gain control over your money or the lack of it will forever  control you. Dave Ramsey",
    "Opportunities don't happen .You create them. Chris Grosser",
    "Don't stay in bed unless you can make money in bed . George Burns",
    "Money often costs too much. Ralph  Waldo Emerson",
    "Never depend on a single  income.  Make an investement to create a second source. Warrem Buffett",
    "It's not about having lots of money; It's about knowing how to manage it. Anonymous",
    "Rich people have small TVS and big libraries, and poor people have small libraries and "
    "Being rich is having money; being wealthy is having time. Margaret Bonnano ",
    "A wise person should  have money in their head, but not in their heart, Jonathon Swift",
    "Money grows on the tree of persistence. Japanese Proverb",
]

@app.get("/side_hustles")
def get_side_hustles(apikey: str):
       """Return a randon side hustle idea"""
       if apikey != "1234567890":
              return {"error": "Invalid API key"}
       return {"side_hustles": random.choice(side_hustles)}
   
@app.get("/money_quotes")
def get_money_quotes(apikey: str):
       """Return a random money quote"""
       if apikey != "1234567890":
           return {"error": "Invalid API KEY"}
       return {"money_quotes": random.choice(money_quotes)}