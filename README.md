## Installation
  ```bash
  git clone https://github.com/DemirSacirovic/taskflow-api.git
  cd taskflow-api
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python3 create_tables.py
  uvicorn app.main:app --reload
  ```

  ## API Documentation
  http://localhost:8000/docs
  
