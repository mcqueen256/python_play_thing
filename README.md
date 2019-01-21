
# Setup Python Environment

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cd elpis-gui`
5. `npm i`
6. `npm run build`
7. `cd ..`
8. `deactivate` (when leaving the development environment)
9. `mkdir uploaded_files`

# Run the Server

1. `source venv/bin/activate`
2. `export FLASK_ENV='development'`
3. `FLASK_APP=ppp.py flask run`
