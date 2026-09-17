import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="Simple Job Portal", page_icon="💼", layout="wide")

@st.cache_resource
def get_supabase() -> Client:
    try:
        return create_client(
            st.secrets["SUPABASE_URL"],
            st.secrets["SUPABASE_KEY"]
        )
    except Exception as e:
        st.error("Supabase connection failed.")
        st.code(str(e))
        st.stop()

supabase = get_supabase()

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- PROFESSIONAL THEME ----------------
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 75% 10%, rgba(37,99,235,.22), transparent 30%),
        linear-gradient(135deg,#020617 0%,#071329 55%,#020617 100%);
    color:#f8fafc;
}
section[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#020817,#061225);
    border-right:1px solid #1e3a8a;
}
section[data-testid="stSidebar"] * { color:#f8fafc; }
.block-container { max-width:1250px; padding-top:2rem; }
.hero-title { font-size:clamp(42px,6vw,68px); font-weight:800; line-height:1.02; }
.gradient-text {
    background:linear-gradient(90deg,#60a5fa,#6366f1,#c084fc);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.hero-subtitle { font-size:23px; color:#dbeafe; margin:16px 0; }
.hero-description { max-width:680px; color:#94a3b8; font-size:17px; line-height:1.8; }
.feature-card {
    padding:26px; min-height:245px; border-radius:20px;
    background:linear-gradient(145deg,rgba(15,29,56,.96),rgba(8,18,38,.96));
    margin-bottom:12px;
}
.blue-card { border:1px solid #2563eb; }
.green-card { border:1px solid #10b981; }
.purple-card { border:1px solid #9333ea; }
.feature-title { font-size:25px; font-weight:750; margin-bottom:20px; }
.feature-line { color:#dbe4f5; margin:13px 0; font-size:15px; }
.stat-card {
    text-align:center; padding:22px 10px; border-radius:16px;
    background:rgba(11,23,48,.9); border:1px solid #23395d;
}
.stat-number { font-size:34px; font-weight:800; }
.stat-label { color:#94a3b8; }
.page-card {
    padding:28px; border-radius:20px;
    background:rgba(7,20,43,.92); border:1px solid #214b8d;
}
.small-muted { color:#94a3b8; }
.stButton > button {
    width:100%; min-height:44px; border-radius:10px;
    border:1px solid #3b82f6;
    background:linear-gradient(90deg,#2563eb,#4f46e5);
    color:white; font-weight:650;
}
.stButton > button:hover {
    border-color:#93c5fd;
    box-shadow:0 0 22px rgba(59,130,246,.30);
}
div[data-testid="stForm"] {
    background:rgba(7,20,43,.92);
    border:1px solid #214b8d;
    border-radius:18px;
    padding:24px;
}
#MainMenu, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ---------------- HELPERS ----------------
def go(page):
    st.session_state.page = page
    st.rerun()

def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.page = "Home"
    st.rerun()

def current_user():
    return st.session_state.user

def logged_in():
    return bool(st.session_state.logged_in and st.session_state.user)

def is_role(role):
    return logged_in() and current_user().get("role") == role

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💼 Job Portal")
    st.divider()

    if not logged_in():
        menu = st.radio(
            "Navigation",
            ["🏠 Home", "📝 Register", "🔐 Login"],
            label_visibility="collapsed"
        )
        st.session_state.page = {
            "🏠 Home":"Home",
            "📝 Register":"Register",
            "🔐 Login":"Login"
        }[menu]
    else:
        u = current_user()
        st.success(f"Welcome, {u.get('full_name','User')}")
        st.caption(
            "Role: " +
            ("Job Seeker" if u.get("role") == "job_seeker" else "Recruiter")
        )
        st.divider()

        if u.get("role") == "job_seeker":
            menu = st.radio(
                "Navigation",
                ["🏠 Dashboard", "🔎 View Jobs", "🚪 Logout"],
                label_visibility="collapsed"
            )
            mapping = {
                "🏠 Dashboard":"Dashboard",
                "🔎 View Jobs":"View Jobs",
                "🚪 Logout":"Logout"
            }
        else:
            menu = st.radio(
                "Navigation",
                ["🏠 Dashboard", "➕ Create Job", "📋 My Jobs", "🚪 Logout"],
                label_visibility="collapsed"
            )
            mapping = {
                "🏠 Dashboard":"Dashboard",
                "➕ Create Job":"Create Job",
                "📋 My Jobs":"My Jobs",
                "🚪 Logout":"Logout"
            }

        selected = mapping[menu]
        if selected == "Logout":
            logout()
        st.session_state.page = selected

# ---------------- HOME ----------------
def home():
    left, right = st.columns([1.05,.95], gap="large")

    with left:
        st.markdown("""
<div class="hero-title">Simple<br><span class="gradient-text">Job Portal</span></div>
<div class="hero-subtitle">Find jobs. Hire talent. Build careers.</div>
<div class="hero-description">
A professional platform connecting job seekers with great opportunities
and recruiters with talented candidates.
</div>
""", unsafe_allow_html=True)

        st.write("")
        c1,c2 = st.columns(2)
        with c1:
            if st.button("🚀 Get Started", key="home_get_started" , use_container_width=True):
                 st.session_state.selected_role = "Job Seeker"

                 go("Register")
        with c2:
            if st.button("🔐 Login", key="home_login"):
                go("Login")

    with right:
        st.markdown("""
<div class="page-card" style="text-align:center; min-height:280px;">
<div style="font-size:95px;">💻</div>
<h2 style="color:#93c5fd;">Find Your Dream Job</h2>
<p class="small-muted">Search opportunities from top companies</p>
<div style="background:#111c33;padding:14px;border-radius:10px;">
🔍 Job title or keyword &nbsp;&nbsp; 📍 Location
</div>
</div>
""", unsafe_allow_html=True)

    st.write("")
    a,b,c = st.columns(3)

    with a:
        st.markdown("""
<div class="feature-card blue-card">
<div class="feature-title">👤 Job Seeker</div>
<div class="feature-line">🔵 Create an account</div>
<div class="feature-line">🔵 Login securely</div>
<div class="feature-line">🔵 View available jobs</div>
<div class="feature-line">🔵 Find opportunities</div>
</div>
""", unsafe_allow_html=True)
        if st.button("Job Seeker → Register", key="home_seeker"):

            st.session_state.selected_role = "Job Seeker"

            go("Register")

    with b:
        st.markdown("""
<div class="feature-card green-card">
<div class="feature-title">🏢 Recruiter</div>
<div class="feature-line">🟢 Create an account</div>
<div class="feature-line">🟢 Login</div>
<div class="feature-line">🟢 Publish jobs</div>
<div class="feature-line">🟢 Manage posted jobs</div>
</div>
""", unsafe_allow_html=True)
        if st.button("Recruiter → Register", key="home_recruiter"):
             
             st.session_state.selected_role = "Recruiter"

             go("Register")

    with c:
        st.markdown("""
<div class="feature-card purple-card">
<div class="feature-title">🛡️ Security</div>
<div class="feature-line">🟣 Role-based access</div>
<div class="feature-line">🟣 Protected pages</div>
<div class="feature-line">🟣 Logout anytime</div>
<div class="feature-line">🟣 Supabase database</div>
</div>
""", unsafe_allow_html=True)

    st.write("")
    st.markdown("## 📊 Platform Highlights")
    x1,x2,x3,x4 = st.columns(4)
    for col,number,label in [
        (x1,"10K+","Active Jobs"),
        (x2,"5K+","Happy Users"),
        (x3,"500+","Companies"),
        (x4,"100%","Trusted")
    ]:
        with col:
            st.markdown(
                f'<div class="stat-card"><div class="stat-number">{number}</div>'
                f'<div class="stat-label">{label}</div></div>',
                unsafe_allow_html=True
            )

# ---------------- REGISTER ----------------
def register():
    st.markdown("## 📝 Create Your Account")
    st.markdown(
        '<p class="small-muted">Join the Job Portal and start your journey.</p>',
        unsafe_allow_html=True
    )

    with st.form("register_form"):
        full_name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")
        role = st.selectbox("Select Role", ["Job Seeker","Recruiter"])
        submitted = st.form_submit_button("Create Account", use_container_width=True)

    if submitted:
        full_name = full_name.strip()
        email = email.strip().lower()

        if not all([full_name,email,password,confirm]):
            st.error("Please fill all fields.")
            return
        if "@" not in email:
            st.error("Please enter a valid email.")
            return
        if password != confirm:
            st.error("Passwords do not match.")
            return

        role_value = "job_seeker" if role == "Job Seeker" else "recruiter"

        try:
            existing = (
                supabase.table("users")
                .select("id,email")
                .eq("email",email)
                .limit(1)
                .execute()
            )

            if existing.data:
                st.warning("This email is already registered.")
                if st.button("🔐 Go to Login", key="register_to_login"):
                    go("Login")
                return

            supabase.table("users").insert({
                "full_name":full_name,
                "email":email,
                "password":password,
                "role":role_value
            }).execute()

            st.success("🎉 Account created successfully!")
            st.balloons()
            st.info("Your account is ready. Please login.")

            if st.button("🔐 Continue to Login", key="after_register"):
                go("Login")

        except Exception as e:
            st.error("Registration failed.")
            st.code(str(e))

# ---------------- LOGIN ----------------
def login():
    st.markdown("## 🔐 Welcome Back")
    st.markdown(
        '<p class="small-muted">Login to access your Job Portal account.</p>',
        unsafe_allow_html=True
    )

    with st.form("login_form"):
        email = st.text_input("Email", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        email = email.strip().lower()

        if not email or not password:
            st.error("Please enter email and password.")
            return

        try:
            result = (
                supabase.table("users")
                .select("id,full_name,email,password,role")
                .eq("email",email)
                .limit(1)
                .execute()
            )

            if not result.data:
                st.error("Invalid email or password.")
                return

            account = result.data[0]

            # Normal password comparison - no hashing.
            if account.get("password") != password:
                st.error("Invalid email or password.")
                return

            st.session_state.logged_in = True
            st.session_state.user = account
            st.session_state.page = "Dashboard"

            st.success("🎉 Login successful!")
            st.rerun()

        except Exception as e:
            st.error("Login failed.")
            st.code(str(e))

# ---------------- DASHBOARD ----------------
def dashboard():
    u = current_user()
    name = u.get("full_name","User")
    role = u.get("role","")

    st.markdown(
        f'<div class="page-card"><h2>👋 Welcome, {name}</h2>'
        f'<p class="small-muted">Logged in as '
        f'{"Job Seeker" if role=="job_seeker" else "Recruiter"}.</p></div>',
        unsafe_allow_html=True
    )

    st.write("")

    if role == "job_seeker":
        st.info("Find your next opportunity by opening View Jobs.")
        if st.button("🔎 View Available Jobs", key="dashboard_view"):
            go("View Jobs")
    else:
        st.success("Create and manage your job postings.")
        c1,c2 = st.columns(2)
        with c1:
            if st.button("➕ Create Job", key="dashboard_create"):
                go("Create Job")
        with c2:
            if st.button("📋 My Jobs", key="dashboard_my"):
                go("My Jobs")

# ---------------- CREATE JOB ----------------
def create_job():
    if not is_role("recruiter"):
        st.error("Only recruiters can create jobs.")
        return

    st.markdown("## ➕ Create a New Job")
    st.markdown(
        '<p class="small-muted">Publish an opportunity for job seekers.</p>',
        unsafe_allow_html=True
    )

    u = current_user()

    with st.form("create_job_form", clear_on_submit=True):
        title = st.text_input("Job Title", placeholder="Python Developer")
        company = st.text_input("Company Name", placeholder="ABC Technologies")
        location = st.text_input("Location", placeholder="Hyderabad")
        salary = st.text_input("Salary", placeholder="₹5 - ₹8 LPA")
        description = st.text_area(
            "Job Description",
            placeholder="Describe the role, skills and responsibilities...",
            height=180
        )
        submitted = st.form_submit_button("🚀 Publish Job", use_container_width=True)

    if submitted:
        values = [
            title.strip(), company.strip(), location.strip(),
            salary.strip(), description.strip()
        ]

        if not all(values):
            st.error("Please fill all job fields.")
            return

        try:
            supabase.table("jobs").insert({
                "title":values[0],
                "company":values[1],
                "location":values[2],
                "salary":values[3],
                "description":values[4],
                "recruiter_email":u["email"]
            }).execute()

            st.success("🎉 Job created successfully!")
            st.balloons()

        except Exception as e:
            st.error("Unable to create job.")
            st.code(str(e))

# ---------------- JOB CARD ----------------
# IMPORTANT: Native Streamlit components are used here.
# This fixes the old problem where <div>, <b>, etc. appeared as text.
def show_job(job):
    with st.container(border=True):
        st.markdown(f"### 💼 {job.get('title','Untitled Job')}")
        c1,c2,c3 = st.columns(3)

        with c1:
            st.write(f"🏢 **Company:** {job.get('company','-')}")
        with c2:
            st.write(f"📍 **Location:** {job.get('location','-')}")
        with c3:
            st.write(f"💰 **Salary:** {job.get('salary','-')}")

        st.write("📝 **Description**")
        st.write(job.get("description","-"))

# ---------------- VIEW JOBS ----------------
def view_jobs():
    if not is_role("job_seeker"):
        st.error("Only job seekers can view jobs.")
        return

    st.markdown("## 💼 Available Jobs")
    st.markdown(
        '<p class="small-muted">Latest opportunities posted by recruiters.</p>',
        unsafe_allow_html=True
    )

    try:
        result = (
            supabase.table("jobs")
            .select(
                "id,title,company,location,salary,description,"
                "recruiter_email,created_at"
            )
            .order("created_at",desc=True)
            .execute()
        )

        jobs = result.data or []

        if not jobs:
            st.info("No jobs are available yet.")
            return

        st.success(f"{len(jobs)} job(s) available")

        for job in jobs:
            show_job(job)
            st.write("")

    except Exception as e:
        st.error("Unable to load jobs.")
        st.code(str(e))

# ---------------- MY JOBS ----------------
def my_jobs():
    if not is_role("recruiter"):
        st.error("Only recruiters can view their jobs.")
        return

    st.markdown("## 📋 My Posted Jobs")
    st.markdown(
        '<p class="small-muted">Jobs posted from your recruiter account.</p>',
        unsafe_allow_html=True
    )

    try:
        result = (
            supabase.table("jobs")
            .select(
                "id,title,company,location,salary,description,"
                "recruiter_email,created_at"
            )
            .eq("recruiter_email",current_user()["email"])
            .order("created_at",desc=True)
            .execute()
        )

        jobs = result.data or []

        if not jobs:
            st.info("You have not posted any jobs yet.")
            if st.button("➕ Create Your First Job", key="first_job"):
                go("Create Job")
            return

        st.success(f"You have posted {len(jobs)} job(s).")

        for job in jobs:
            show_job(job)
            st.write("")

    except Exception as e:
        st.error("Unable to load your jobs.")
        st.code(str(e))

# ---------------- ROUTER ----------------
page = st.session_state.page

if page == "Home":
    home()
elif page == "Register":
    register()
elif page == "Login":
    login()
elif page == "Dashboard":
    if logged_in():
        dashboard()
    else:
        go("Login")
elif page == "View Jobs":
    if is_role("job_seeker"):
        view_jobs()
    else:
        st.error("Access denied. Job Seekers only.")
elif page == "Create Job":
    if is_role("recruiter"):
        create_job()
    else:
        st.error("Access denied. Recruiters only.")
elif page == "My Jobs":
    if is_role("recruiter"):
        my_jobs()
    else:
        st.error("Access denied. Recruiters only.")
else:
    go("Home")
