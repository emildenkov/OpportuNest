# OpportuNest

## Deployed: opportunest-ffh3cuh7cyhyhhbh.italynorth-01.azurewebsites.net

## Overview

OpportuNest is Django Web Application, which connects employers and employees all over the world. The job-seekers can browse through different job offers and apply for the job, which they like. Companies can publish on the platform if they have open postions and approve or reject applications from the job-seekers. 


## Installation Guide
1. Python 3.12 required
   
2. Clone the repository:
   ```sh
   git clone 
   ```

3. Create venv and install the requirements:
   ```sh
   pip install -r requirements.txt 
   ```

4. Check the .env.template file for the needed credentials
   - If you use MacOS or Linux you don't need the `CELERYD_POOL`. For Windows it should be setted to `solo`

5. Run the Celery worker in separated terminal:
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
      - **Email:** denkov_it@gmail.com; **password:** 12company34
      - **Email:** georgigeorgiev2@gmail.com; **password:** 12seeker34
