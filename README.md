# Django Password Generator

This is a Django project that generates random passwords based on user preferences.

## Getting Started

To get started with this project, follow the instructions below.

### Prerequisites

- Python 
- Django 

### Installation

1. Clone the repository:

   shell
   git clone https://github.com/mldias23i/django3-password-generator.git
   
2. Navigate to the project directory:

   cd django3-password-generator


###Configuration

1. Create a local_settings.py file in the password_generator directory.

2. Open the local_settings.py file and add the following content:

  SECRET_KEY = '<your-secret-key>'

  Replace <your-secret-key> with your own secret key. Make sure to keep it confidential and do not share it publicly. 
  Check the file additional_instructions.md to see how can you access your own secret key.

  
###Running the Application
  
 1. Apply the database migrations:

    python manage.py migrate

 2. Start the development server:

    python manage.py runserver

3. Open your web browser and access the application at http://localhost:8000.


###Usage
  
  Enter your password preferences on the homepage and click "Generate Password" to get a randomly generated password.

