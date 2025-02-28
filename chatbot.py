import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your actual Segment API Key
SEGMENT_API_KEY = "JUQ76MZC5MWXYBATYH8ZA16Y"

# Base URL for Segment API
SEGMENT_API_BASE_URL = "https://api.segment.io/v1"

# Headers for authentication
HEADERS = {
    "Authorization": f"Basic {SEGMENT_API_KEY}",
    "Content-Type": "application/json"
}

def fetch_sources():
    """Fetch the list of sources from Segment."""
    url = f"{SEGMENT_API_BASE_URL}/sources"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else {"error": response.text}

def create_source(source_name):
    """Create a new source in Segment."""
    url = f"{SEGMENT_API_BASE_URL}/sources"
    payload = {"name": source_name, "enabled": True}
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json() if response.status_code == 201 else {"error": response.text}

@app.route("/chatbot", methods=["POST"])
def chatbot():
    """Main chatbot API endpoint."""
    data = request.json
    query = data.get("question", "").lower()

    if not query:
        return jsonify({"error": "No question provided."}), 400

    # Handling "how-to" questions for Segment
    if "set up a new source" in query:
        response = {"answer": "To set up a new source in Segment, send a POST request to /sources API."}
    elif "fetch sources" in query:
        response = fetch_sources()
    elif "create source" in query:
        source_name = "My New Source"  # You can modify this to take input dynamically
        response = create_source(source_name)
    else:
        response = {"message": "Please ask about Segment API-related tasks."}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
