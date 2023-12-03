UML Sequence Diagram Description
Actors and Components:

Client/User Interface: The interface where users interact, typically a web browser.
Flask Web Application: Your Flask server, handling requests and responses.
Google Books API: The external API service providing book data.
Database: The database where notes are stored (for / route).
Flow for Search Functionality (/search Route):

User to Flask App:
The user inputs a search query in the UI and submits the request.
The Flask app receives the GET request with the search query.
Flask App to Google Books API:
The Flask app constructs a request with the search query and API key.
The request is sent to the Google Books API.
Google Books API to Flask App:
The API processes the request and sends back a response.
The response contains the book data in JSON format.
Flask App to User:
The Flask app processes the JSON data.
It then renders the search.html template with the book data and sends it to the user's browser.
Flow for Adding a Note (/ Route with POST Method):

User to Flask App:
The user submits a note via the UI.
The Flask app receives the POST request with the note data.
Flask App to Database:
The app creates a new Note object and saves it to the database.
Database to Flask App:
The database confirms the successful addition of the note.
Flask App to User:
The Flask app sends a success message and renders the home.html page with the updated notes.
Flow for Deleting a Note (/delete-note Route):

User to Flask App:
The user initiates a note deletion request.
The Flask app receives the POST request with the note ID.
Flask App to Database:
The app queries the database for the note and deletes it.
Database to Flask App:
The database confirms the note deletion.
Flask App to User:
The Flask app sends a JSON response indicating success or failure of the deletion process.

![image](https://github.com/griessmk/FlaskProject--Version-1/assets/122305497/e24474d3-0363-455a-921e-48f3aa95d60f)




COMMUNICATION CONTRACT
Preamble
This communication contract is established to ensure effective collaboration, clear communication, and a positive working relationship between group members for the duration of the software engineering project in our college class. The contract aligns with the ground rules we have previously set and serves as a guide for our interactions.

1. Communication Platform
Primary Platform: Discord will be used as the primary platform for all project-related communication.
Usage Guidelines: Discord channels will be organized for different purposes, such as general updates, task discussions, and meeting arrangements.

2. Responsiveness and Availability
Response Time: All messages or tasks will be acknowledged or responded to within 24 hours.
Delayed Response Notification: In cases of expected delay, the unavailable team member will inform the other in advance, providing an estimated time of response.

3. Meeting Schedule and Etiquette
Regular Meetings: Weekly check-ins will be held every Wednesday at 6 PM PST.
Agenda Preparation: Both members will contribute to setting the agenda for each meeting at least one day in advance.
Cancellation/Rescheduling Policy: If a member cannot attend a scheduled meeting, they should notify the other at least 12 hours in advance and propose an alternative time.

4. Task Allocation and Accountability
Joint Decision-Making: Tasks will be allocated based on mutual agreement, considering each member’s strengths, interests, and availability.
Task Tracking: A shared task tracker (e.g., Trello or Asana) will be used to monitor progress and deadlines.
Revisiting Task Allocation: Any changes in task responsibilities must be discussed and mutually agreed upon.

5. Conflict Resolution
Direct Communication: In case of disagreements, the issue will be addressed directly and respectfully between the team members.
Seeking External Help: If a resolution is not reached, the team will seek guidance from the course instructor or a designated third party.

6. Respect and Professionalism
Mutual Respect: Both team members commit to maintaining a respectful and professional demeanor in all interactions.
Constructive Feedback: Feedback will be given constructively and received openly, with the aim of project improvement.

7. Documentation and Record Keeping
Meeting Minutes: Key points, decisions, and action items from meetings will be documented and shared.
Change Log: Any significant changes in project direction or task allocation will be recorded.

8. Review and Adaptation
Contract Review: This contract will be reviewed bi-weekly to ensure it remains relevant and effective.
Flexibility for Changes: The contract can be modified with mutual consent to adapt to changing project needs or challenges.

