# OpportuNest

### Deployed Application
[OpportuNest Live](https://opportunest-ffh3cuh7cyhyhhbh.italynorth-01.azurewebsites.net)

---


## Installation Guide
1. **Python 3.12 Required**

2. **Clone the Repository**
   ```sh
   git clone https://github.com/emildenkov/OpportuNest.git
   ```

3. **Create venv and install the requirements**:
   ```sh
   pip install -r requirements.txt 
   ```

4. **Check the .env.template file for the needed credentials**
   - If you use MacOS or Linux you don't need the `CELERYD_POOL`. For Windows it should be setted to `solo`

5. **Run the Celery worker in separate terminal**:
   - Command for Windows:
     ```sh
     celery -A OpportuNest worker --pool=solo
     ```
   - Command for MacOS and Linux:
     ```sh
     celery -A OpportuNest worker --loglevel=info
     ```
     
6. **Database**:
   - The database is hosted on Azure and you can access it with the needed credentials. This is done only for the purpose of this project and IT IS NOT RECOMMENDED for projects, which will be used by vast amount of users!!!

7. **Users**:
   - **Superuser**:
      - **Email:** opportunest_superuser@gmail.com; **password:** superuser123
   - **Company staff user**:
      - **Email:** staff_company@gmail.com; **password:** 12staff34
   - **Seeker staff user**:
      - **Email:** staff_seeker@gmail.com; **password:** 12staff34
   - **Regular users**:
      - **Email:** test_it_company@gmail.com; **password:** 12company34
      - **Email:** georgigeorgiev2@gmail.com; **password:** 12seeker34

## How OpportuNest Works

OpportuNest is a Django-based web application designed to connect employers with employees efficiently. Below is an overview of how the platform operates:

### Home Page and Account Registration
- When you open the application, you'll be greeted by the home page, which includes button for `Log In`.
- Clicking on `Log In` redirects you to the login page. If you don’t have an account, click `Register` at the bottom of the login form. 
- During registration, you will select your desired account type (Company or Seeker). This choice will determine the registration form you complete.
- After successful registration, you’ll receive a welcome email and can start using the app.

### Companies
- If you create a company account, you’ll have the following features:
  - Edit and delete your profile.
  - Post job listings.
  - Review job applications.
  - Decide whether to `Accept` or `Reject` applicants based on your preferences.
  - Provide feedback by rating the application.

### Seekers
- If you create a seeker account, you’ll have access to the following features:
  - Edit and delete your profile.
  - Select and update the skills you possess.
  - Apply for jobs.
  - Track application statuses (`Accepted` or `Rejected`) on your profile page.
  - Rate the application.

### REST Endpoint
- OpportuNest includes a REST endpoint that provides access to all posted job listings.

Enjoy using OpportuNest to bridge opportunities between employers and job seekers!
