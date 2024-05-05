### Installing process

**1. Prerequisites:**

- Ensure you have Python (version 3.6 or later) installed on your system. You can verify this by running `python3 --version` or `python --version` in your terminal.
- If you don't have Python, download and install it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

**2. Create a Virtual Environment (Recommended):**

- Using a virtual environment helps isolate project dependencies and avoid conflicts with other Python installations.
- Create a virtual environment using `venv` (Python 3.3+) or `virtualenv` (older versions):

  ```bash
  python3 -m venv my_venv  # Using venv
  # OR
  virtualenv my_venv
  ```

- Activate the virtual environment:

  ```bash
  source my_venv/bin/activate  # Linux/macOS
  # OR
  my_venv\Scripts\activate.bat  # Windows
  ```

**3. Install Django and Graphene-Django:**

- Activate your virtual environment (if you created one).
- Install Django and Graphene-Django using `pip`:

  ```bash
  pip install django graphene-django
  ```

**4. Create a Django Project:**

- Navigate to your desired project directory.
- Use `django-admin startproject` to create a new Django project:

  ```bash
  django-admin startproject django_graphql  # Replace with your project name
  ```

**5. Create a Django App:**

- Inside your project directory (e.g., `django_graphql`), create a new app for your CRUD functionality:

  ```bash
  cd my_crud_app
  django-admin startapp crud_app
  ```

**6. Add the App to `INSTALLED_APPS`:**

- Open your project's `settings.py` file (usually in `my_app/`) with a text editor.
- Find the `INSTALLED_APPS` list and add your newly created app:

  ```python
  INSTALLED_APPS = [
      # ... other installed apps
      'app_app',
  ]
  ```

**7. (Optional) Install GraphiQL (for testing GraphQL queries):**

- If you want to use GraphiQL to test your GraphQL API, install it using `pip`:

  ```bash
  pip install django-graphiql
  ```


**9. (Optional) Database Configuration:**

- Django needs a database to store data. Configure your database settings (e.g., `DATABASES`) in your project's `settings.py` according to your chosen database backend (e.g., PostgreSQL, MySQL). Refer to the Django documentation for specific instructions: [https://docs.djangoproject.com/en/5.0/](https://docs.djangoproject.com/en/5.0/)
- I used here `.sqlite`

**10. Running the Development Server:**

- With your project set up, you can run the development server to test your app:

  ```bash
  python manage.py runserver
  ```

This should start the Django development server, typically accessible at `http://127.0.0.1:8000/` in your web browser. You'll have a basic Django installation ready to begin building your GraphQL CRUD app.

Remember to create your models, serializers (optional), queries, mutations, and schema to implement the CRUD functionality.

For further configuration and usage details, refer to the Django and Graphene-Django documentation:

- Django: [https://docs.djangoproject.com/en/5.0/](https://docs.djangoproject.com/en/5.0/)
- Graphene-Django: [https://graphene-django-murali.readthedocs.io/en/latest/rest-framework.html](https://graphene-django-murali.readthedocs.io/en/latest/rest-framework.html)

### Some basic example of query:
Create Author & Book:
input:
```
mutation {
  createAuthor(name: "Mr. Nas") {
    author {
      id
      name
    }
  },
  createBook(name:"Journey to the center of the earth", authorIds: 1){
    book{
      id,
      name
      authors{
        id
        name
      }
    }
  }
}
```

Response:
```
{
  "data": {
    "createAuthor": {
      "author": {
        "id": "3",
        "name": "Mr. Nas"
      }
    },
    "createBook": {
      "book": {
        "id": "2",
        "name": "Journey to the center of the earth",
        "authors": [
          {
            "id": "1",
            "name": "Mr. Nas"
          }
        ]
      }
    }
  }
}
```

Get All author & books:
```
query{
  authors{
    id
    name
  },
  books{
    name
    authors{
      id
      name
    }
  }
}
```

Response:
```
{
  "data": {
    "authors": [
      {
        "id": "1",
        "name": "Mr. Nas"
      },
      {
        "id": "2",
        "name": "Mr. Nas"
      }
    ],
    "books": [
      {
        "name": "Journey to the center of the earth",
        "authors": [
          {
            "id": "1",
            "name": "Mr. Nas"
          }
        ]
      }
    ]
  }
}
```