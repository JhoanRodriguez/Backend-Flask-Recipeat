# Flask Backend


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt.

```bash
pip install requirements.txt
```

## Usage

```python

You will  need to setup the env variables before to run the app.

Run python3 app.py
The app will be running at localhost:5000
```

## Endpoins
```
GET's Methods:

- /api/recipes -> Getting all data with pagination ( limit and offset required)
example : http://localhost:5000/api/recipes?limit=5&offset=0

- /api/recipes/<id> -> Gettinga recipe from the ID
example : http://localhost:5000/api/recipes/106a9c6a-17e3-11eb-ad9c-560c39725801

- /api/search=<item> -> Search recipes with the ingredients
example :  http://localhost:5000/api/search=pollo,arroz

DELETE Method:

- /api/recipes/<id> -> Delete a recipe from the ID

POST Method

- /api/recipes -> create a new recipe

```


## License
[MIT](https://choosealicense.com/licenses/mit/)
