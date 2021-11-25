# fast-api-postgres-poc
Pre-reqs to run:
1. Create a python virtual environment. Virtual environment give an nice neat isolated environment to run FastAPI.

python3 -m venv venv (this cmd only the first time)
source venv/bin/activate (everytime you want to launch the venv)
export PYTHONPATH=$PWD

2. Install postgres
https://postgresapp.com/ (default settings were used)
type psql in terminal to confirm it exists (try source ~/.bashrc if not recognizing psql)
also execute:
python -m pip install psycopg2-binary
Open your `~/.zshrc` file, and *add* the following line:
```
export PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"
```
then update with cmd: source ~/.zshrc
run psql on terminal, then run:
CREATE DATABASE testdatabase;

The new database should be now showing on the postgres app!

<img width="500" alt="Screen Shot 2021-11-25 at 1 17 17 AM" src="https://user-images.githubusercontent.com/33057640/143413821-e043fa23-a5df-439e-bb90-cc5f51fb93d5.png">

3. Install docker

4. Correct the postgres username, password to yours at main.py and docker-compose.yml.


The api.py exposes Notes. Notes primarily has 3 fields, id, text, completed.

example: id: 2, text: Buy cake, Completed: False

To open swagger just /docs to the URL. Below is a ss.

<img width="500" alt="Screen Shot 2021-11-25 at 1 37 49 AM" src="https://user-images.githubusercontent.com/33057640/143417018-9b7f6444-1c00-4a3f-abcb-a314bc35ce94.png">

<h3>2 ways to run this application - without docker and with docker:</h3>

1. 
ensure postgres has the database and is up and running. Like in pic before
run "pip install -r requirements.txt" This shall install your dependencies
The main.py has been configured to run with Docker, so you need to make some changes in main.py to run without docker. The changes are mentioned in a comment at main.py.

run "python main.py"
Your application shall be at: http://localhost:8080/

2. 
docker-compose up --build (first time and anytime you make changes)
docker-compose up 

from docker apps UI, you can pause the container. 2 services shall be launched, web and db.
Your application shall be at: http://localhost:8008/ 


<img width="500" alt="Screen Shot 2021-11-25 at 1 36 42 AM" src="https://user-images.githubusercontent.com/33057640/143416880-48d2d947-d5a3-44f2-aa29-546e9ffd36f8.png">


