from flask import Flask, render_template, jsonify
from datetime import datetime
from pytz import timezone, UnknownTimeZoneError

# Initiating Flask application
app = Flask(__name__)

@app.route("/")
def time():
    now = datetime.now(timezone('America/New_York'))
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")
    year = now.strftime("%Y")
    return render_template("index.html", date=date, time=time, year=year)

@app.route("/update_time/<path:tz_name>")
def update_time(tz_name):
    try:
        tz = timezone(tz_name)
        now = datetime.now(tz)
        return jsonify({
            "date": now.strftime("%d-%m-%Y"),
            "time": now.strftime("%H:%M:%S"),
            "year": now.strftime("%Y")
        })
    except UnknownTimeZoneError:
        return jsonify({"error": "Invalid timezone"}), 404

if __name__ == "__main__":
    app.run(debug=True)