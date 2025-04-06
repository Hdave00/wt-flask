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

@app.route("/update_time/<timezone_name>")
def update_time(timezone_name):
    try:
        # Get the current time in the requested timezone
        tz = timezone(timezone_name)
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d-%m-%Y")
        return jsonify({"time": time, "date": date, "year": now.strftime("%Y")})
    except UnknownTimeZoneError:
        # Handle the case where the timezone is not valid
        return jsonify({"error": "Unknown timezone"}), 400

if __name__ == "__main__":
    app.run(debug=True)