# tasks
## Setup
### 1. Create and run virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
### 2. Install packages
```bash
pip install -r requirements
```
### 3. Run the database service
```bash
sudo docker-compose up
```
### 4. Start the application
```bash
gunicorn tasks.wsgi --bind 0.0.0.0:8000
```

## Running tests
To run the tests be sure that the database service is up and running and simply run:
```bash
pytest
```

## API docs
The documentation for the API is located under the address: 127.0.0.1:8000/docs
