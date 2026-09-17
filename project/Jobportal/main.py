import json
from pathlib import Path


# ============================================================
# FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "user.json"
JOBS_FILE = BASE_DIR / "jobs.json"


# ============================================================
# JSON HELPER FUNCTIONS
# ============================================================

def load_data(filename):
    """Read data from a JSON file."""

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError, OSError):
        return []


def save_data(filename, data):
    """Save data into a JSON file."""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def next_id(records):
    """Return an ID higher than every valid integer ID in records."""

    ids = [record["id"] for record in records
           if isinstance(record, dict) and isinstance(record.get("id"), int)]
    return max(ids, default=0) + 1


def read_input(prompt):
    """Read terminal input without crashing when input is unavailable."""

    try:
        return input(prompt).strip()
    except EOFError:
        return None


# ============================================================
# USER CLASS
# ============================================================

class User:

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def to_dict(self, user_id):
        """Convert User object into dictionary for JSON."""

        return {
            "id": user_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": self.role
        }


# ============================================================
# JOB CLASS
# ============================================================

class Job:

    def __init__(
        self,
        title,
        company,
        location,
        salary,
        description,
        recruiter_id
    ):
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.description = description
        self.recruiter_id = recruiter_id

    def to_dict(self, job_id):
        """Convert Job object into dictionary for JSON."""

        return {
            "id": job_id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "salary": self.salary,
            "description": self.description,
            "recruiter_id": self.recruiter_id
        }


# ============================================================
# JOB PORTAL CLASS
# ============================================================

class JobPortal:

    def __init__(self):
        self.users = load_data(USERS_FILE)
        self.jobs = load_data(JOBS_FILE)
        self.current_user = None

    # ========================================================
    # REGISTER
    # ========================================================

    def register(self):

        print("\n========== REGISTER ==========")

        name = read_input("Enter your name: ")
        email = read_input("Enter your email: ")
        password = read_input("Enter your password: ")

        # Check empty fields
        if name is None or email is None or password is None:
            print("\nInput ended. Returning to the main menu.")
            return

        if not name or not email or not password:
            print("❌ All fields are required.")
            return

        # Check existing email
        for user in self.users:
            if isinstance(user, dict) and user.get("email", "").lower() == email.lower():
                print("❌ Email already registered.")
                return

        print("\nSelect Role")
        print("1. Job Seeker")
        print("2. Recruiter")

        choice = read_input("Enter choice: ")

        if choice is None:
            print("\nInput ended. Returning to the main menu.")
            return

        if choice == "1":
            role = "job_seeker"

        elif choice == "2":
            role = "recruiter"

        else:
            print("❌ Invalid role.")
            return

        # Generate user ID
        user_id = next_id(self.users)

        user = User(
            name,
            email,
            password,
            role
        )

        user_data = user.to_dict(user_id)

        self.users.append(user_data)

        save_data(
            USERS_FILE,
            self.users
        )

        print("\n✅ Registration successful!")
        print(f"Your User ID is: {user_id}")
        print(f"Your Role is: {role}")

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self):

        print("\n========== LOGIN ==========")

        email = read_input("Enter email: ")
        password = read_input("Enter password: ")

        if email is None or password is None:
            print("\nInput ended. Returning to the main menu.")
            return

        for user in self.users:

            if (
                isinstance(user, dict)
                and user.get("email", "").lower() == email.lower()
                and user.get("password") == password
            ):

                self.current_user = user

                print("\n✅ Login successful!")
                print(f"Welcome, {user['name']}!")

                if user.get("role") == "job_seeker":
                    self.job_seeker_menu()

                elif user.get("role") == "recruiter":
                    self.recruiter_menu()

                return

        print("\n❌ Invalid email or password.")

    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self):

        if self.current_user:

            print(
                f"\n👋 Goodbye, {self.current_user['name']}!"
            )

            self.current_user = None

    # ========================================================
    # JOB SEEKER MENU
    # ========================================================

    def job_seeker_menu(self):

        while self.current_user:

            print("\n================================")
            print("        JOB SEEKER MENU")
            print("================================")
            print("1. View Jobs")
            print("2. Logout")

            choice = read_input("Enter choice: ")

            if choice is None:
                self.logout()
                return

            if choice == "1":

                self.view_jobs()

            elif choice == "2":

                self.logout()

            else:

                print("❌ Invalid choice.")

    # ========================================================
    # RECRUITER MENU
    # ========================================================

    def recruiter_menu(self):

        while self.current_user:

            print("\n================================")
            print("        RECRUITER MENU")
            print("================================")
            print("1. Create Job")
            print("2. View My Jobs")
            print("3. Logout")

            choice = read_input("Enter choice: ")

            if choice is None:
                self.logout()
                return

            if choice == "1":

                self.create_job()

            elif choice == "2":

                self.view_my_jobs()

            elif choice == "3":

                self.logout()

            else:

                print("❌ Invalid choice.")

    # ========================================================
    # CREATE JOB
    # ========================================================

    def create_job(self):

        # Route protection
        if not self.current_user:
            print("❌ Please login first.")
            return

        # Role protection
        if self.current_user["role"] != "recruiter":
            print("❌ Only recruiters can create jobs.")
            return

        print("\n========== CREATE JOB ==========")

        title = read_input("Job Title: ")
        company = read_input("Company Name: ")
        location = read_input("Location: ")
        salary = read_input("Salary: ")
        description = read_input("Job Description: ")

        if None in (title, company, location, salary, description):
            print("\nInput ended. Returning to the recruiter menu.")
            return

        if not title or not company or not location:
            print("❌ Title, company and location are required.")
            return

        # Generate job ID
        job_id = next_id(self.jobs)

        job = Job(
            title,
            company,
            location,
            salary,
            description,
            self.current_user["id"]
        )

        job_data = job.to_dict(job_id)

        self.jobs.append(job_data)

        save_data(
            JOBS_FILE,
            self.jobs
        )

        print("\n✅ Job created successfully!")
        print(f"Job ID: {job_id}")

    # ========================================================
    # VIEW ALL JOBS
    # ========================================================

    def view_jobs(self):

        # Route protection
        if not self.current_user:
            print("❌ Please login first.")
            return

        if self.current_user.get("role") != "job_seeker":
            print("❌ Only job seekers can view all jobs.")
            return

        print("\n================================")
        print("          AVAILABLE JOBS")
        print("================================")

        if not self.jobs:
            print("No jobs available.")
            return

        for job in self.jobs:

            print("\n--------------------------------")
            print(f"Job ID     : {job['id']}")
            print(f"Title      : {job['title']}")
            print(f"Company    : {job['company']}")
            print(f"Location   : {job['location']}")
            print(f"Salary     : {job['salary']}")
            print(f"Description: {job['description']}")
            print("--------------------------------")

    # ========================================================
    # VIEW RECRUITER'S JOBS
    # ========================================================

    def view_my_jobs(self):

        # Route protection
        if not self.current_user:
            print("❌ Please login first.")
            return

        # Role protection
        if self.current_user["role"] != "recruiter":
            print("❌ Only recruiters can view their jobs.")
            return

        print("\n================================")
        print("          MY JOBS")
        print("================================")

        my_jobs = []

        for job in self.jobs:

            if (isinstance(job, dict)
                    and job.get("recruiter_id") == self.current_user.get("id")):
                my_jobs.append(job)

        if not my_jobs:
            print("You haven't created any jobs yet.")
            return

        for job in my_jobs:

            print("\n--------------------------------")
            print(f"Job ID     : {job['id']}")
            print(f"Title      : {job['title']}")
            print(f"Company    : {job['company']}")
            print(f"Location   : {job['location']}")
            print(f"Salary     : {job['salary']}")
            print(f"Description: {job['description']}")
            print("--------------------------------")

    # ========================================================
    # MAIN MENU
    # ========================================================

    def main_menu(self):

        while True:

            print("\n================================")
            print("        SIMPLE JOB PORTAL")
            print("================================")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = read_input("\nEnter choice: ")

            if choice is None:
                print("\nInput ended. Exiting Job Portal.")
                break

            if choice == "1":

                self.register()

            elif choice == "2":

                self.login()

            elif choice == "3":

                print("\nThank you for using Job Portal!")
                break

            else:

                print("❌ Invalid choice. Please try again.")


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():

    portal = JobPortal()

    portal.main_menu()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()

