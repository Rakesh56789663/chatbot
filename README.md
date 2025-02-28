Segment API Chatbot

Overview

This chatbot is built using Flask and Segment API to answer "how-to" questions related to Segment. It can:

Fetch a list of sources from Segment.

Create a new source in Segment.

Provide basic guidance on Segment API usage.

Prerequisites

Python 3.x installed

Segment API Key

Required Python packages installed

Installation

Clone the repository:

git clone https://github.com/your-repo/segment-chatbot.git
cd segment-chatbot

Install dependencies:

pip install flask requests

Set up Segment API Key:

Open chatbot.py

Replace SEGMENT_API_KEY with your actual Segment API key.

Running the Chatbot

Start the Flask application:

python chatbot.py

By default, the server will run on http://127.0.0.1:5000/.

API Endpoints

1. /chatbot (POST)

Request Format

{
  "question": "How do I set up a new source in Segment?"
}

Response Examples

Fetch Sources:

{
  "sources": [
    {
      "id": "src_123",
      "name": "My Website",
      "createdAt": "2023-01-01T12:00:00Z"
    }
  ]
}

Create Source:

{
  "id": "src_456",
  "name": "My New Source",
  "enabled": true
}

Invalid Question:

{
  "message": "Please ask about Segment API-related tasks."
}

Future Enhancements

Extend support for mParticle, Lytics, and Zeotap APIs.

Implement cross-CDP comparisons.

Deploy on AWS/GCP.

License

This project is open-source and available under the MIT License.

Author

[Your Name]
