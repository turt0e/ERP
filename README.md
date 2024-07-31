# Enterprise Resource Planning (ERP) for Soda Distribution

## Streamlining Operations from Stock to Sales

### Description
To develop and deploy a comprehensive Python-based ERP system tailored for wholesale soda distribution, integrating advanced functionalities such as real-time dashboard and reporting for inventory and sales insights, enhanced sales and customer management tools, automated inventory tracking, streamlined account and credit management, and a user-friendly interface to optimize operational efficiency, customer satisfaction, and financial management.

### Features
- **Account Management (Authorization)**: Users can create, edit, and delete accounts with specified access levels. Role-based permissions ensure security and control over data access, safeguarding sensitive information.
- **Product Management**: Users can easily add new products, update details, and track historical changes.
- **Sales Management**: Track sales and generate reports.
- **Stock Management (Inventory)**: Monitor and manage stock levels.
- **Expense Management**: Record and manage business expenses.
- **Sales Invoice**: Generate and manage sales invoices.
- **Credit Memory**: Track credit transactions.
- **CRM System**: Manage customer relationships and interactions.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/turt0e/ERP.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ERP 
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv/Scripts/activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Usage
1. Access the application in your web browser at `http://127.0.0.1:8000/`.
2. Log in with the superuser credentials you created.
3. Start managing your soda distribution operations through the various features available.

### Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes.
4. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
5. Push to the branch:
    ```bash
    git push ERP feature-name
    ```
6. Open a pull request.

### Naayos napo yung dashboard before deadline pero di po nasama sa progress report pdf.
