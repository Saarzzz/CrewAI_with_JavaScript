from flask import Flask, request, jsonify
import crews  # Assuming crew.py is in the same directory

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

@app.route("/api/crewA", methods=["POST"])
def research():
    data = request.get_json()  # Get prospect and reason from JSON data
    prospect = data.get("prospect")
    reason = data.get("reason")

    if not prospect or not reason:
        return jsonify({"error": "Missing prospect or reason"}), 400

    Context = f"Prospect: {prospect} \n Reason for Outreach: {reason}"

    research_crew = crews.ResearchCrew(job_id="your_unique_job_id")  # Replace with unique ID generation
    research_crew.setup_crew(Context)
    results = research_crew.kickoff()

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=3001)