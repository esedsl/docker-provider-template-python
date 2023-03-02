# Dont update this file either , it is just a wrapper to run the app in dev mode
from app import app

app.run(host='0.0.0.0', port=8080,debug=True)