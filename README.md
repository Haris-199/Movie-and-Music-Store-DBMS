This was done for bonus marks

# Steps to run our Web Application

1. Setup a virtual environment
    ```
    Windows: py -m venv venv
    Unix/MacOS: python -m venv venv
    ```

2. Activate environment
    ```
    Windows: venv\Scripts\activate.bat 
    Unix/MacOS: source venv/bin/activate
    ```

3. Install packages
    ```
    pip install -r requirements.txt
    ```

4. Apply migrations

    Make sure you’re in the “/project” directory and run 
    ```
    python manage.py migrate
    ```

5. Load sample data

    Make sure you’re in the “/project” directory and run
    ```
    python manage.py loaddata sample_data/all.json 
    ```

6. Run server

    Make sure you’re in the “/project” directory and run 
    ```
    python manage.py runserver 
    ```
    Next visit "localhost:8000" on your browser. 
    
    To deactivate the virtual environment, type "deactivate" in your terminal.
