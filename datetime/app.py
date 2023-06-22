# Python flask app to display IST and UTC time on the browser
## Author : Ramesh Babu 
## Date : 29 Nov 2022
## File : app.py
## Type : Python Flask app

from flask import Flask, render_template
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone

app = Flask(__name__)

@app.route('/')
def hello():
    format = "%d-%m-%Y %H:%M:%S  %Z%z"
    now_utc = datetime.now(timezone('UTC'))
    now_local = now_utc.astimezone(get_localzone())
    ist_now = now_local.strftime(format)
    templateData = {
        'title':'Time_n_Date_IST!',
        'now_utc':now_utc,
        'time':now_local
        }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
