# Anonymous Help Hub

**Anonymous Help Hub** is a privacy-focused web application designed to connect people who need help with people who are willing to provide help — without requiring users to reveal their real identity.

The project provides an anonymous environment where users can post help requests, discover open requests, get matched with helpers, and communicate through anonymous messages.

> **Project:** Anonymous Help Hub
> **Repository:** `tejswi317-cloud/Anonymous_Help_Hub`
> **Technology:** Python + Flask + SQLite

---

##  Features

###  Anonymous Identity

Every visitor is automatically assigned a randomly generated anonymous identity such as:

```text
Quiet Sparrow 421
```

The application generates identities using combinations of adjectives, nouns, and random numbers. Users therefore do not need to provide their real name to participate.

###  Create a Help Request

Users can create a request by providing:

* Category
* Title
* Description

The application validates the submitted information and limits the size of questions and messages.

###  Browse Open Requests

Users can view currently open help requests posted by other anonymous users.

Requests are stored with a status such as:

```text
open
matched
```

###  Anonymous Matching

A user can choose to help another anonymous user.

The matching system:

1. Checks that the requested question exists.
2. Checks that the request is still open.
3. Prevents users from matching with their own request.
4. Creates a helper/asker match.
5. Changes the question status to `matched`.

###  Anonymous Messaging

After users are matched, they can communicate through anonymous messages associated with the match.

The application stores:

* Match ID
* Sender's anonymous ID
* Message
* Timestamp

###  SQLite Database

The application uses SQLite for local data storage.

The database contains tables for:

* Questions
* Matches
* Messages

The database is automatically initialized when the Flask application starts.

---

##  Technology Stack

| Technology | Purpose                                |
| ---------- | -------------------------------------- |
| Python     | Core programming language              |
| Flask      | Web application framework              |
| SQLite     | Database                               |
| HTML       | Web page structure                     |
| CSS        | User interface styling                 |
| Jinja2     | Flask template rendering               |
| Git/GitHub | Version control and repository hosting |

The repository currently contains the main Python modules `app.py`, `anonymous.py`, `config.py`, `database.py`, `matching.py`, and `models.py`, together with `templates`, `static`, and `requirements.txt`.

---

##  Project Structure

```text
Anonymous_Help_Hub/
│
├── app.py
├── anonymous.py
├── config.py
├── database.py
├── matching.py
├── models.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── ask.html
│   ├── question.html
│   └── ...
│
└── static/
    ├── css/
    ├── js/
    └── ...
```

### Main Python Files

#### `app.py`

The main Flask application.

It handles:

* Application startup
* Anonymous sessions
* Routes
* Help-request submission
* Matching
* Messaging
* Template rendering

Every visitor receives an anonymous identity through the Flask session.

#### `anonymous.py`

Responsible for generating random anonymous identities.

Example:

```text
Calm River 572
Friendly Cloud 314
Brave Phoenix 821
```

The identity generator combines predefined adjectives and nouns with a random three-digit number.

#### `database.py`

Handles SQLite database operations including:

* Database initialization
* Creating questions
* Retrieving questions
* Updating question status
* Creating matches
* Retrieving matches
* Storing messages
* Retrieving messages

The database currently defines `questions`, `matches`, and `messages` tables.

#### `matching.py`

Contains the matching logic between a person asking for help and a person offering help.

It prevents a user from helping their own question and changes a successfully matched request from `open` to `matched`.

#### `config.py`

Contains application configuration including:

```text
SECRET_KEY
DATABASE
MAX_QUESTION_LENGTH
MAX_MESSAGE_LENGTH
```

The default SQLite database is `help_hub.db`.

---

#  Installation

## 1. Clone the Repository

```bash
git clone https://github.com/tejswi317-cloud/Anonymous_Help_Hub.git
```

Move into the project directory:

```bash
cd Anonymous_Help_Hub
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

Start the Flask application with:

```bash
python app.py
```

If the project is configured to expose Flask's development server, open the local address displayed in the terminal, commonly:

```text
http://127.0.0.1:5000
```

---

#  Configuration

The application uses environment variables for configuration.

Example:

### Windows Command Prompt

```cmd
set SECRET_KEY=your-secret-key
set DATABASE=help_hub.db
```

### PowerShell

```powershell
$env:SECRET_KEY="your-secret-key"
$env:DATABASE="help_hub.db"
```

For production deployment, use a strong randomly generated `SECRET_KEY` rather than the development fallback.

---

#  How the Application Works

The basic workflow is:

```text
                ┌─────────────────┐
                │      Visitor    │
                └────────┬────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Anonymous Identity  │
              │ Generated           │
              └─────────┬───────────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
      ┌──────────────┐      ┌──────────────┐
      │ Ask for Help │      │ Browse Help  │
      └──────┬───────┘      │ Requests     │
             │              └──────┬───────┘
             ▼                     │
      ┌──────────────┐             │
      │ SQLite DB    │◄────────────┘
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │ Helper Match │
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │ Anonymous    │
      │ Messaging    │
      └──────────────┘
```

---

#  Privacy Concept

Anonymous Help Hub is designed around identity minimization.

Instead of requiring a user's real name, the application creates an anonymous session identity.

For example:

```text
User's real identity
        ↓
   Not displayed
        ↓
Anonymous Help Hub
        ↓
"Hopeful Moon 731"
```

### Important

**Anonymous identity does not automatically mean complete technical anonymity.**

A production deployment should consider additional privacy and security measures such as:

* HTTPS
* Secure session cookies
* Strong secret keys
* Database protection
* Access controls
* Input sanitization
* Rate limiting
* Abuse reporting
* Logging policies
* Data retention policies

---

#  Development

To modify the project:

```bash
git clone https://github.com/tejswi317-cloud/Anonymous_Help_Hub.git
cd Anonymous_Help_Hub
```

Create and activate a virtual environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

After making changes:

```bash
git add .
git commit -m "Update Anonymous Help Hub"
git push origin main
```

---

#  Future Improvements

Possible future versions could include:

* User-controlled anonymous profiles
* Better category filtering
* Search functionality
* Notifications
* Real-time messaging
* File/image attachments
* Help-request priority levels
* Request closing/completion
* Abuse reporting
* Moderation tools
* CAPTCHA/rate limiting
* Improved authentication options
* Production database support
* Docker support
* Automated testing
* Deployment configuration
* Accessibility improvements
* Progressive Web App support

---

#  Contributing

Contributions are welcome.

A typical contribution workflow is:

```bash
git checkout -b feature/your-feature
```

Make your changes and test them locally.

Then:

```bash
git add .
git commit -m "Add your feature"
git push origin feature/your-feature
```

Open a Pull Request on GitHub.

---

#  Disclaimer

Anonymous Help Hub is an educational and community-oriented software project.

It should not be considered a replacement for:

* Emergency services
* Medical professionals
* Mental-health professionals
* Law-enforcement services
* Professional financial or legal advice

For emergencies, users should contact the appropriate local emergency or professional service.

---

#  License

No license file is currently shown in the repository. If this project is intended to be open source, add an appropriate `LICENSE` file before formally distributing or reusing the software.

---

#  Project

**Anonymous Help Hub**

Repository:

https://github.com/tejswi317-cloud/Anonymous_Help_Hub

Built with using Python and Flask.
