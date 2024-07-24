# PROJECT: Hệ thống thu thập dữ liệu
## Project Structure
```
my_gradio_project/
├── data/
│ └── dataset.csv # Data files
├── models/
│ └── model.pkl # Trained models
├── src/
│ ├── init.py # Makes src a Python package
│ ├── data_processing.py # Data processing scripts
│ ├── model.py # Model training and prediction scripts
│ ├── api.py # API interaction scripts
│ └── app.py # Gradio app script
├── notebooks/
│ └── analysis.ipynb # Jupyter notebooks for data analysis
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Git ignore file
```
### `data/`
- Contains data files used in the project.

### `models/`
- Contains trained models.

### `src/`
- **`__init__.py`**: Makes `src` a Python package and includes necessary imports.
- **`data_processing.py`**: Functions for loading and preprocessing data.
- **`model.py`**: Functions for training the model and making predictions.
- **`api.py`**: Functions for interacting with external APIs.
- **`app.py`**: Main Gradio app script that defines the web interface.

### `notebooks/`
- Contains Jupyter notebooks for data analysis and experiments.

### `requirements.txt`
- Lists all the dependencies required for the project.

### `README.md`
- Project documentation.

### `.gitignore`
- Specifies files and directories to be ignored by Git.

## Dependencies

Install the necessary dependencies using pip:

```sh
pip install -r requirements.txt