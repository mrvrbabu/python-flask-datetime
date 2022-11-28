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
        'title' : 'Time_n_Date_IST!',
        'now_utc'   : now_utc,
        'time' : ist_now
        }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)