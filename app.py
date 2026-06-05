from datetime import datetime
from flask import Flask, render_template, request, Response
import joblib
import sqlite3
import csv

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("tfidf_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    entered_url = ""
    analysis = None
    recommendations = None

    if request.method == "POST":

        entered_url = request.form["url"]

        url_vector = vectorizer.transform([entered_url])

        prediction = model.predict(url_vector)[0]

        probabilities = model.predict_proba(url_vector)

        confidence = round(
            max(probabilities[0]) * 100,
            2
        )

        if prediction == "phishing":

            recommendations = [

                "Do not enter passwords",

                "Verify website ownership",

                "Check SSL certificate",

                "Avoid clicking suspicious links"

            ]

        else:

            recommendations = [

                "HTTPS detected",

                "No obvious warning signs",

                "Domain appears legitimate",

                "Continue browsing cautiously"

            ]


        # Save scan history
        conn = sqlite3.connect("history.db")

        cursor = conn.cursor()

        current_time = datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

        cursor.execute(
            """
            INSERT INTO scans(
                url,
                prediction,
                scan_time
            )
            VALUES(?, ?, ?)
            """,
            (
                entered_url,
                prediction,
                current_time
            )
        )

        conn.commit()
        conn.close()

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        entered_url=entered_url,
        recommendations=recommendations
    )

@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("history.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM scans")
    total_scans = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM scans WHERE prediction='phishing'"
    )
    phishing_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM scans WHERE prediction='benign'"
    )
    benign_count = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT url, prediction, scan_time
        FROM scans
        ORDER BY id DESC
        LIMIT 5
        """
    )

    recent_scans = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total_scans=total_scans,
        phishing_count=phishing_count,
        benign_count=benign_count,
        recent_scans=recent_scans
    )


@app.route("/history")
def history():

    conn = sqlite3.connect("history.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM scans
        ORDER BY id DESC
        """
    )

    scans = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        scans=scans
    )

@app.route("/export")
def export():

    conn = sqlite3.connect("history.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM scans
        ORDER BY id DESC
        """
    )

    scans = cursor.fetchall()

    conn.close()

    def generate():

        yield "ID,URL,Prediction,Date & Time\n"

        for scan in scans:

            yield (
                f"{scan[0]},"
                f"{scan[1]},"
                f"{scan[2]},"
                f"{scan[3]}\n"
            )

    return Response(
        generate(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=scan_history.csv"
        }
    )

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/analytics")
def analytics():

    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM scans WHERE prediction='benign'"
    )
    benign_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM scans WHERE prediction='phishing'"
    )
    phishing_count = cursor.fetchone()[0]

    total_scans = benign_count + phishing_count

    conn.close()

    return render_template(
        "analytics.html",
        total_scans=total_scans,
        benign_count=benign_count,
        phishing_count=phishing_count
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



