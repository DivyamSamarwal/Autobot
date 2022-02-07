#SERVER
from flask import Flask

from threading import Thread



app = Flask('')



@app.route('/')

def home():

    return "AutoBot"



def run():

  app.run(host='IP Here',port="Must be an integer")



def keep_alive():  

    t = Thread(target=run)

    t.start()
