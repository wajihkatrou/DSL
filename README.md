This application is a small domain specific language implemented using django and django rest-frameworks.

# Installation
The used packaging tool is [pipenv](https://pipenv-fork.readthedocs.io/en/latest/). 
To install the application, simply navigate to **Botify_Challenge** folder and run: **pipenv install**.

# Run
To run the application, navigate to **domain_specific_language** directory and run **python manage.py runserver**. 

# Routes
The exposed routes are:
	**/cities** to preview the list of cities in the database.
	**/sql** to enter the JSON query and return the correspondant SQL query.

# Front-end
The rendred interfaces are the default rest-framework ViewSet and APIView. To Post a city or a JSON query, simply use the given post form.