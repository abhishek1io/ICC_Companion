"""Take screenshots of ICC Companion pages via Playwright."""
import os, json
from playwright.sync_api import sync_playwright

BASE = "http://localhost/ICC_Companion"
OUT = r"C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report"
os.makedirs(OUT, exist_ok=True)

def shot(page, name, full=True):
    path = os.path.join(OUT, f"screenshot_{name}.png")
    page.screenshot(path=path, full_page=full)
    print(f"  [OK] {name}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1280, "height": 800})
    page = context.new_page()

    # 1. HOME PAGE
    print("\n1. Public Pages:")
    page.goto(f"{BASE}/index.html")
    shot(page, "home")

    # 2. STUDENT LOGIN
    page.goto(f"{BASE}/student-login.html")
    shot(page, "student_login")

    # 3. ADMIN LOGIN
    page.goto(f"{BASE}/admin-login.html")
    shot(page, "admin_login")

    # === LOGIN AS STUDENT ===
    print("\n2. Student Portal (after login):")
    page.goto(f"{BASE}/student-login.html")
    page.fill("#rollNumber", "UT-231-049-0001")
    page.fill("#dob", "2005-01-01")
    page.click("button[type='submit']")
    page.wait_for_timeout(3000)

    # 4. STUDENT DASHBOARD
    if "dashboard" in page.url:
        shot(page, "student_dashboard")

        # 5. MY SUBJECTS
        page.goto(f"{BASE}/student/subjects.html")
        page.wait_for_timeout(2000)
        shot(page, "subjects")

        # 6. MY ATTENDANCE
        page.goto(f"{BASE}/student/attendance.html")
        page.wait_for_timeout(2000)
        shot(page, "attendance")

        # 7. EXAM TIMETABLE
        page.goto(f"{BASE}/student/exams.html")
        page.wait_for_timeout(2000)
        shot(page, "exams")

        # 8. LOST & FOUND
        page.goto(f"{BASE}/student/lost-found.html")
        page.wait_for_timeout(2000)
        shot(page, "lost_found")

        # 9. ANNOUNCEMENTS
        page.goto(f"{BASE}/student/announcements.html")
        page.wait_for_timeout(2000)
        shot(page, "announcements")

        # 10. RESOURCES
        page.goto(f"{BASE}/student/resources.html")
        page.wait_for_timeout(2000)
        shot(page, "resources")
    else:
        page.screenshot(path=os.path.join(OUT, "screenshot_login_fail.png"))
        print("  [FAIL] Student login did not redirect to dashboard")

    # === LOGIN AS ADMIN ===
    print("\n3. Admin Portal (after login):")
    page.goto(f"{BASE}/admin-login.html")
    page.wait_for_timeout(1000)
    # Click Principal tab first
    page.click("#principalTab")
    page.wait_for_timeout(500)
    page.fill("#username", "admin")
    page.fill("#password", "admin123")
    page.click("button[type='submit']")
    page.wait_for_timeout(3000)

    if "dashboard" in page.url:
        shot(page, "admin_dashboard")

        # 12. MANAGE STUDENTS
        page.goto(f"{BASE}/admin/students.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_students")

        # 13. ATTENDANCE MANAGEMENT
        page.goto(f"{BASE}/admin/attendance.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_attendance")

        # 14. MANAGE EXAMS
        page.goto(f"{BASE}/admin/exams.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_exams")

        # 15. MANAGE ANNOUNCEMENTS
        page.goto(f"{BASE}/admin/announcements.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_announcements")

        # 16. MANAGE FACULTY
        page.goto(f"{BASE}/admin/staff.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_faculty")

        # 17. MANAGE DEPARTMENTS
        page.goto(f"{BASE}/admin/departments.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_departments")

        # 18. MANAGE ROUTINES
        page.goto(f"{BASE}/admin/routines.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_routines")

        # 19. MANAGE LOST & FOUND
        page.goto(f"{BASE}/admin/lost-found.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_lost_found")

        # 20. MANAGE RESOURCES
        page.goto(f"{BASE}/admin/resources.html")
        page.wait_for_timeout(2000)
        shot(page, "manage_resources")
    else:
        page.screenshot(path=os.path.join(OUT, "screenshot_admin_fail.png"))
        print("  [FAIL] Admin login did not redirect to dashboard")

    browser.close()
    print("\nAll screenshots taken!")
