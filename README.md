# Edu Summarizer

This tool exposes an API to summarize large text inputs into byte-sized chunks. It uses OpenAIs GPT-3 model to accomplish this.

## Installing
Start with cloning this repo

[Recommended] Using a virtual environment
```
pip install virtualenv

virtualenv venv
```
To activate your virtualenv
```
source ./venv/bin/activate
```

Install the required dependencies
```
pip install -r requirements.txt
```

To exit the virtual environment
```
deactivate
```

## Running in local

### Debug mode

```
python main.py
```

### Non-debug mode

```
python app.py
```
