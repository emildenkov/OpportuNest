# OpportuNest

### Deployed: opportunest-ffh3cuh7cyhyhhbh.italynorth-01.azurewebsites.net

### Overview

OpportuNest is Django Web Application, which connects employers and employees all over the world. The job-seekers can browse through different job offers and apply for the job, which they like. Companies can publish on the platform if they have open postions and approve or reject applications from the job-seekers. 


## Installation Guide
1. Python 3.12 required
   
2. Clone the repository:
   ```sh
   git clone https://github.com/emildenkov/OpportuNest.git
   ```

3. Create venv and install the requirements:
   ```sh
   pip install -r requirements.txt 
   ```

4. Check the .env.template file for the needed credentials
   - If you use MacOS or Linux you don't need the `CELERYD_POOL`. For Windows it should be setted to `solo`

5. Run the Celery worker in separate terminal:
   - Command for Windows:
     ```sh
     celery -A OpportuNest worker --pool=solo
     ```
   - Command for MacOS and Linux:
     ```sh
     celery -A OpportuNest worker --loglevel=info
     ```
     
6. Database:
   - The database is hosted on Azure and you can access it with the needed credentials. This is done only for the purpose of this project and IT IS NOT RECOMMENDED for projects, which will be used by vast amount of users!!!

7. Users:
   - **Superuser**:
      - **Email:** opportunest_superuser@gmail.com; **password:** superuser123
   - **Company staff user**:
      - **Email:** staff_company@gmail.com; **password:** 12staff34
   - **Seeker staff user**:
      - **Email:** staff_seeker@gmail.com; **password:** 12staff34
   - **Regular users**:
      - **Email:** test_it_company@gmail.com; **password:** 12company34
      - **Email:** georgigeorgiev2@gmail.com; **password:** 12seeker34

## How OpportuNest works:
- OpportuNest is a Django based web app, which main purpose is to connect employers with employees.
- When you open the application you will see the home page and button for `Log in` and you will be redirected to the logging page. If you don't have an account you should click on `Register`, which is in the bottom of the form. Then you will   see a form in which you will have to select the desired type of account that you want and this will lead you to the registration form for your account type.
- After registration you will recieve a welcome email and be able to operate in the app.
- Companies:
      - If you chose a company account, you will be able to edit and delete your profile, post jobs, review applications and based on your oppinion you will decide if you want to `Accept` or `Reject` the applicant. You have the permission            to rate the app also.
-Seekers:
      - If you chose a seeker account, you will be able to edit and delete your profile as you can select the skills, which you posses. You will be able to apply for jobs and see if you are `Accepted` or `Rejected` from your profile page and         you also have the permission to rate the app
- REST endpoint:
      - There is a REST endpoint which serves all jobs, that have been posted.
