  # Saransh - Text Summarizer

  This tool exposes an API to summarize large text inputs into byte-sized chunks. It uses OpenAIs GPT-3 model to accomplish this.
  
  
  ## Try it out
  
  Try out the API with our [demo backend](https://ai-summarizer.herokuapp.com/) or from our [webapp](https://paulfaraday.github.io/ai-summarizer/)


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

  ### Debug mode

  ```
  python main.py
  ```

  ### Non-debug mode

  ```
  python app.py
  ```

## API Documentation
The API documentation is available in `/docs`

| Endpoint | Documentation |
|----------|---------------|
|/summary|text_summary.md|
|/pdfSummary|pdf_summary.md|
