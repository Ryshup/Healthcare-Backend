# Healthcare Backend Project

This project is a backend application for managing patients, doctors, and user authentication in a healthcare system.

## Folder Structure

- **patients/**: Contains models, views, serializers, and URLs related to patients and doctors.
- **users/**: Handles user registration, login, and JWT-based authentication.
- **venv/**: The virtual environment containing all dependencies for the project.
- **healthcare/**: The main Django project folder that includes the settings and configurations.

## How to Run

1. Clone the repository.
2. Set up a virtual environment and activate it:
   - `python -m venv venv`
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install dependencies using: `pip install -r requirements.txt`.
4. Apply database migrations: `python manage.py migrate`.
5. Start the development server: `python manage.py runserver`.

## API Endpoints

- `POST /api/auth/register/`: Register a new user.
- `POST /api/auth/login/`: Login and get a JWT token.
- `GET /api/patients/`: List all patients.
- `POST /api/patients/`: Create a new patient.
- `GET /api/doctors/`: List all doctors.
- `POST /api/doctors/`: Create a new doctor.
- `POST /api/mappings/`: Assign a doctor to a patient.

