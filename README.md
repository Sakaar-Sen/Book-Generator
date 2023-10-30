# Book Generator
 
# Steps To Run
- Install dependencies by running
  ```
  pip install langchain markdown pdfkit requests streamlit pandas numpy python-dotenv
  ```
- Get a [Huggingface](https://huggingface.co/) API KEY and set it as an env variable "HUGGING_FACE_APIKEY" in a .env file
- Download [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) and if you change the default path during installation, set it in line 172 in bookgen.py
- Now you are ready to start the app. Simply run
  ```
  streamlit run app.py
  ```
