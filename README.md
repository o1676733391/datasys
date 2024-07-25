# DataSys Project

## Description
This project is a sample application using Gradio for the front-end and Flask for the back-end.

## Installation
```sh
pip install -r requirements.txt
```
## Running the Application
```sh
python src/datasys/backend/server.py
python src/datasys/frontend/app.py
```
## Running Tests
```sh
python -m unittest discover -s tests
```
## Project Structure
```sh
datasys/
├── data/
│   ├── example/
│   │   ├── walk.jpg
│   │   └── run-11239.mp3
├── src/
│   ├── datasys/
│   │   ├── __init__.py
│   │   ├── frontend/
│   │   │   ├── __init__.py
│   │   │   └── app.py
│   │   ├── backend/
│   │   │   ├── __init__.py
│   │   │   └── server.py
├── tests/
│   ├── __init__.py
│   ├── test_app.py
├── README.md
├── requirements.txt
├── setup.py
└── .gitignore
```
