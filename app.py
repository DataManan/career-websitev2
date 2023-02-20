from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {  
    "ID": 1,
    "ROLE": "Data Analyst",
    "LOCATION": "Bengaluru, India",
    "PAY": "Rs. 10,00,000"
  },
  {  
    "ID": 2,
    "ROLE": "Data Scientist",
    "LOCATION": "Mumbai, India",
    "PAY": "Rs. 15,00,000"
  },
  {  
    "ID": 3,
    "ROLE": "Frontend Engineer",
    "LOCATION": "Bengaluru, India",
    "PAY": "Rs. 12,00,000"
  },
  {  
    "ID": 4,
    "ROLE": "Backend Engineer",
    "LOCATION": "San Francisco, U.S.A.",
    "PAY": "$ 120,000"
  }
]

@app.route("/")
def home_page():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def jobs_page():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)