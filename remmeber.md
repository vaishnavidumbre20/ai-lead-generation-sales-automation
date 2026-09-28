# in a new PowerShell window (this shell will run uvicorn)
cd C:\Users\user\Desktop\gsbgProject\leads-op-main

# set SMTP env vars in this shell (use your NEW app password)
$env:EMAIL_ADDRESS = "your.email@gmail.com"
$env:EMAIL_PASSWORD = ""

# start the server from this same shell (so it inherits the env)
.\.venv\Scripts\Activate
python -m uvicorn app:app --port 8000 --reload