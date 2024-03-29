# Mobile Factory Project

The Mobile Factory project is a Django-based application that simplifies the process of creating orders for mobile devices. It provides a RESTful API built using Django REST Framework (DRF) for handling order creation and management.

## Project Structure

The project directory structure is organized as follows:

- **mobile_factory/**: Main Django project directory.
  - **enums.py**: Defines enums for input types, component types, and components.
  - **errors.py**: Contains custom error classes for the project.
  - **constants.py**: Defines dictionaries mapping input types to prices, component names to component type, and input types to component types.
  - **data_classes.py**: Contains data classes for API responses and controllers.
  - **controllers/**: Folder containing controller logic for handling order creation and management.
  - **tests/**: Folder containing unit tests for the project.
  - **serializers.py**: Contains serializers for creating orders.
  - Other standard Django project files and folders.

## Installation and Setup

1. **Clone the Repository**:

    ```
    git clone <repository-url>
    ```

2. **Setup Virtual Environment**:

    - Create a virtual environment:
    
        ```
        python -m venv venv
        ```

    - Activate the virtual environment:
    
        - On Windows:
        
            ```
            venv\Scripts\activate
            ```

        - On Unix or MacOS:
        
            ```
            source venv/bin/activate
            ```

3. **Install Dependencies**:

    ```
    pip install -r requirements.txt
    ```



5. **Run the Server**:

    Start the Django development server:

    ```
    python manage.py runserver
    ```

6. **Run Tests**:

    Execute unit tests to ensure everything is working as expected:

    ```
    python manage.py test
    ```


## Testing

Unit tests are provided in the `tests/` directory. Run `python manage.py test` to execute the tests and ensure code quality.
