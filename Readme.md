### 📧 Email Verification Web App (Python + Flask + HTML/CSS/JS)

A simple **Email Verification Web Application** built using 

- **Python**
- **Flask (Backend)**
- **HTML**
- **CSS**
- **JavaScript (Frontend)**

The app validates an email address using custom logic and displays the result instantly on the web page.

---
## Table of Contents
- <a href="#Features">Features</a>
- <a href="#Technologies Used">Technologies Used</a>
- <a href="#Project Structure">Project Structure</a>
- <a href="#Installation & Setup">Installation & Setup</a>
- <a href="#API Endpoint">API Endpoint</a>
- <a href="#API Response">API Response</a>
- <a href="#Email Validation Rules">Email Validation Rules</a>
- <a href="#Testing Tools">Testing Tools</a>
- <a href="#Future Improvements">Future Improvements</a>
- <a href="#Author">Author</a>

---
<h2><a class="anchor" id="Features"></a>Features</h2>

- Custom email validation logic (no regex)
- Frontend form with real-time result display
- Flask REST API
- Fetch API for backend communication
- CORS enabled (frontend–backend connection)
- Clean and simple UI

---
<h2><a class="anchor" id="Technologies Used"></a>Technologies Used</h2>

- Frontend
  - HTML5
  - CSS
  - avaScript

- Backend
  - Python 
  - Flask
  - Flask-CORS

--- 
<h2><a class="anchor" id="Project Structure"></a>Project Structure</h2>

email-verification/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── working.js
│
├── backend/
│   └── app.py
│
└── README.md

---
<h2><a class="anchor" id="Installation & Setup"></a>Installation & Setup</h2>

- Clone the Repository

  - git clone https://github.com/your-username/email-verification.git
  - cd email-verification

- Backend Setup (Flask)

  - Create Virtual Environment (Optional)
    - python -m venv venv
    - source venv/bin/activate     # Mac/Linux
    - venv\Scripts\activate        # Windows

  - Install Dependencies
    - pip install flask flask-cors

  - Run Flask Server
    - python app.py

  - Backend will start at: 
    - http://127.0.0.1:5000

- Frontend Setup 
  - Open index.html in your browser
  - OR use Live Server in VS Code for best experience

--- 
<h2><a class="anchor" id="API Endpoint"></a>API Endpoint</h2>

- POST /verify
  - Request Type
    - application/x-www-form-urlencoded
- Parameter
  - Key	
    - email

  - Description
    - Email to validate

- Example Request (JS)

  fetch("http://127.0.0.1:5000/verify", {
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    body: "email=test@gmail.com"
  });

---
<h2><a class="anchor" id="API Response"></a>API Response</h2>

- Valid Email
  {
  "status": "success",
  "message": "Right email"
  }

- Invalid Email
  {
  "status": "error",
  "message": "Wrong email"
  }

---
<h2><a class="anchor" id="Email Validation Rules"></a>Email Validation Rules</h2>

- Minimum length 6 characters
- Must start with an alphabet
- Must contain exactly one @
- Must contain . at -3 or -4 position
- No spaces allowed
- No uppercase letters allowed
- Allowed characters:
  - lowercase letters
  - numbers
  - _ . @

---
<h2><a class="anchor" id="Testing Tools"></a>Testing Tools</h2>

- Browser (Frontend UI)
- Postman
- Thunder Client (VS Code)

--- 
<h2><a class="anchor" id="Future Improvements"></a>Future Improvements</h2>

- Regex-based validation
- Email domain verification
- Better UI animations
- Deployment (Render / Vercel)
- Toast notifications

----
## Author

Ram Krishna
- Email: ramkrishna000888@gmail.com
- Linkeddin: https://www.linkedin.com/in/ramkrishna000/

