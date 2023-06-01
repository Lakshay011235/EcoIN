# EcoIN
A place where you can find all the answers related to your environment concerns.

# Installiation
### Requirements
PIP installed in your local system.

Fork / Download this respository to you local computer.
### Fork
After Forking,
create a new folder in you local computer
Then type the following commands
```
git init
```
```
git clone https://github.com/<GitHub Username>/EcoIN
```
### Download
Directly download the repository

VirtualEnvironment is suggested. So incase if you dont have a virtual environment
```
pip install virtualenvwrapper
```
Now create a new virtual environment.
In this case I am calling my virtual environment as `VirtualEnv`.
```
python -m venv VirtualEnv
```

If you already has an existing virtual environment then activate it by
```
<Your_environment_name>\Scripts\activate
```

Now install the requirements (this is a one time command, no need to run this again).
```
pip install -r requirements.txt
```

# Running the code
Navigate to the directory which has `manage.py` in it.
In this case it is in backend
i.e `.../EcoIn/backend`
then type
```
python manage.py runserver
```

You can view the website at
```
localhost:8000   or http://127.0.0.1:8000
```