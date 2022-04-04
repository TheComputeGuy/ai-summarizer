  # AI Summarizer

  This tool exposes an API to summarize large text inputs into byte-sized chunks. It uses OpenAIs GPT-3 model to accomplish this.

  ## Installing
  Start with cloning this repo
  
  ### [Optional - Recommended] Using a virtual environment
  
  Install and setup virtual environment
  ```
  pip install virtualenv

  virtualenv venv
  ```
  
  To activate your virtualenv
  ```
  source ./venv/bin/activate
  ```

  To exit the virtual environment
  ```
  deactivate
  ```
  
  ### App setup

  Install the required dependencies
  ```
  pip install -r requirements.txt
  ```

  ## Running in local

  ### Environment variables

  Add the following environment variables for the app to work:
  
  | Variable | Description |
  |----------|-------------|
  |OPENAI_API_KEY|The OpenAI API key. [Generate here](https://openai.com/api/)|
  |HCAPTCHA_SECRET|The hcaptcha secret corresponding to the sitekey used in frontend. [Generate here](https://www.hcaptcha.com/)|

  ### Debug mode

  ```
  python main.py
  ```

  ### Non-debug mode

  ```
  python app.py
  ```
