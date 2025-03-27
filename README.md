Hello stranger,

I made this project to showcase a simple solution for short-term memory in AI. 

This Ai will remember everything in the current session, but whenever the api is restarted the conversation will be cleared.

**Setup vitual environment**

If you currently dont have a .venv or base file please use this command to create one.

On Mac:
```
python3 -m venv base
```

On Windows:
```
python -m venv base
```

When the file is created, you can enter the virtual environment like this.

On Mac:
```
source base/bin/activate  
```

On Windows:
```
base/Scripts/activate
```

**Relevant imports**

For relevant imports use this command:

```
pip install -r requirements.txt
```

For adding additional imports to the requirements file use this command:

```
pip freeze > requirements.txt
```

**How to run the application**

This project is using fast api, with uvicorn.

To run access the api endpoint use this command:

```
uvicorn main:app --reload
```
