from fastapi import FastAPI
import json

obj = FastAPI()


# =====================================================
# HOME
# =====================================================

@obj.get("/")
def home():
    return {
        "msg": "Welcome to Job Portal"
    }


# =====================================================
# USER APIs
# =====================================================

# =====================================================
# LOGIN USER
# =====================================================

@obj.post("/login")
def login_user(login_data: dict):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:

        if user["email"] == login_data["email"]:

            if user["password"] == login_data["password"]:

                return {
                    "msg": "Login successful",
                    "login": True,
                    "name": user["name"],
                    "email": user["email"],
                    "role": user["role"]
                }

            return {
                "msg": "Invalid password",
                "login": False
            }

    return {
        "msg": "Email not found",
        "login": False
    }


# =====================================================
# GET ALL USERS
# =====================================================

@obj.get("/get_all_users")
def get_all_users():

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    users = []

    for user in all_users:

        users.append({
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        })

    return users


# =====================================================
# CREATE USER
# =====================================================

@obj.post("/create_user")
def create_user(new_user: dict):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    # Check email already exists
    for user in all_users:

        if user["email"] == new_user["email"]:

            return {
                "msg": "Email already exists"
            }

    # Add new user
    all_users.append(new_user)

    # Save data
    with open("users.json", "w") as w_file:

        json.dump(
            all_users,
            w_file,
            indent=4
        )

    return {
        "msg": "User created successfully"
    }


# =====================================================
# GET SINGLE USER
# =====================================================

# Example:
# /users?email=ravi@gmail.com

@obj.get("/users")
def get_single_user(email: str):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:

        if user["email"] == email:

            return user

    return {
        "msg": "User not found"
    }


# =====================================================
# DELETE USER
# =====================================================

# Example:
# /delete_user/ravi@gmail.com

@obj.delete("/delete_user/{email}")
def delete_user(email: str):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:

        if user["email"] == email:

            all_users.remove(user)

            with open("users.json", "w") as w_file:

                json.dump(
                    all_users,
                    w_file,
                    indent=4
                )

            return {
                "msg": "User deleted successfully"
            }

    return {
        "msg": "User not found"
    }


# =====================================================
# UPDATE USER
# =====================================================

# Example:
# PUT /update_user/ravi@gmail.com

@obj.put("/update_user/{email}")
def update_user(email: str, update_data: dict):

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:

        if user["email"] == email:

            user["name"] = update_data["name"]
            user["password"] = update_data["password"]

            with open("users.json", "w") as w_file:

                json.dump(
                    all_users,
                    w_file,
                    indent=4
                )

            return {
                "msg": "User updated successfully"
            }

    return {
        "msg": "User not found"
    }


# =====================================================
# JOB APIs
# =====================================================

# =====================================================
# RECRUITER CREATE JOB
# =====================================================

@obj.post("/create_job")
def create_job(new_job: dict):

    # Read jobs
    with open("jobs.json", "r") as r_file:
        all_jobs = json.load(r_file)

    # Create job ID
    if len(all_jobs) == 0:

        job_id = 1

    else:

        job_id = all_jobs[-1]["job_id"] + 1

    # Add job ID
    new_job["job_id"] = job_id

    # Add job
    all_jobs.append(new_job)

    # Save jobs
    with open("jobs.json", "w") as w_file:

        json.dump(
            all_jobs,
            w_file,
            indent=4
        )

    return {
        "msg": "Job created successfully",
        "job": new_job
    }


# =====================================================
# JOB SEEKER VIEW ALL JOBS
# =====================================================

@obj.get("/get_all_jobs")
def get_all_jobs():

    with open("jobs.json", "r") as r_file:
        all_jobs = json.load(r_file)

    return all_jobs


# =====================================================
# GET SINGLE JOB
# =====================================================

# Example:
# /jobs/1

@obj.get("/jobs/{job_id}")
def get_single_job(job_id: int):

    with open("jobs.json", "r") as r_file:
        all_jobs = json.load(r_file)

    for job in all_jobs:

        if job["job_id"] == job_id:

            return job

    return {
        "msg": "Job not found"
    }


# =====================================================
# RECRUITER VIEW THEIR JOBS
# =====================================================

# Example:
# /recruiter/jobs?email=recruiter@gmail.com

@obj.get("/recruiter/jobs")
def get_recruiter_jobs(email: str):

    with open("jobs.json", "r") as r_file:
        all_jobs = json.load(r_file)

    my_jobs = []

    for job in all_jobs:

        if job["recruiter_email"] == email:

            my_jobs.append(job)

    return my_jobs


# =====================================================
# JOB SEEKER APPLY FOR JOB
# =====================================================

@obj.post("/apply_job")
def apply_job(application: dict):

    # Read applications
    with open("applications.json", "r") as r_file:
        applications = json.load(r_file)

    # Check duplicate application
    for old_application in applications:

        if (
            old_application["job_id"]
            == application["job_id"]
            and
            old_application["jobseeker_email"]
            == application["jobseeker_email"]
        ):

            return {
                "msg": "You already applied for this job"
            }

    # Check whether job exists
    with open("jobs.json", "r") as r_file:
        all_jobs = json.load(r_file)

    job_found = False

    for job in all_jobs:

        if job["job_id"] == application["job_id"]:

            job_found = True
            break

    if job_found == False:

        return {
            "msg": "Job not found"
        }

    # Create application ID
    if len(applications) == 0:

        application_id = 1

    else:

        application_id = (
            applications[-1]["application_id"] + 1
        )

    # Add application ID
    application["application_id"] = application_id

    # Add application
    applications.append(application)

    # Save application
    with open("applications.json", "w") as w_file:

        json.dump(
            applications,
            w_file,
            indent=4
        )

    return {
        "msg": "Application submitted successfully",
        "application": application
    }


# =====================================================
# JOB SEEKER VIEW THEIR APPLICATIONS
# =====================================================

# Example:
# /my_applications?email=venkatesh@gmail.com

@obj.get("/my_applications")
def my_applications(email: str):

    with open("applications.json", "r") as r_file:
        applications = json.load(r_file)

    my_applications = []

    for application in applications:

        if application["jobseeker_email"] == email:

            my_applications.append(application)

    return my_applications


# =====================================================
# RECRUITER VIEW APPLICATIONS
# =====================================================

# Example:
# /job_applications?recruiter_email=recruiter@gmail.com

@obj.get("/job_applications")
def job_applications(recruiter_email: str):

    # Read jobs
    with open("jobs.json", "r") as r_file:
        all_jobs = json.load(r_file)

    # Read applications
    with open("applications.json", "r") as r_file:
        applications = json.load(r_file)

    # Find recruiter's job IDs
    recruiter_job_ids = []

    for job in all_jobs:

        if job["recruiter_email"] == recruiter_email:

            recruiter_job_ids.append(
                job["job_id"]
            )

    # Find applications for those jobs
    recruiter_applications = []

    for application in applications:

        if application["job_id"] in recruiter_job_ids:

            recruiter_applications.append(
                application
            )

    return recruiter_applications