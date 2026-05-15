"""Generate DFD and ER diagrams for ICC Companion report."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1000, 700
BG = (255, 255, 255)
BLUE = (37, 99, 235)
DARK = (30, 41, 59)
GRAY = (100, 116, 139)
LGRAY = (241, 245, 249)
GREEN = (22, 163, 74)
ORANGE = (234, 88, 12)
RED = (220, 38, 38)

# Try to get a font
def get_font(size):
    try:
        return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)
    except:
        try:
            return ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", size)
        except:
            return ImageFont.load_default()

def rounded_rect(draw, xy, r, fill, outline=None, width=2):
    x1, y1, x2, y2 = xy
    draw.pieslice([x1, y1, x1+2*r, y1+2*r], 180, 270, fill=fill, outline=outline, width=width)
    draw.pieslice([x2-2*r, y1, x2, y1+2*r], 270, 360, fill=fill, outline=outline, width=width)
    draw.pieslice([x1, y2-2*r, x1+2*r, y2], 90, 180, fill=fill, outline=outline, width=width)
    draw.pieslice([x2-2*r, y2-2*r, x2, y2], 0, 90, fill=fill, outline=outline, width=width)
    draw.rectangle([x1+r, y1, x2-r, y2], fill=fill, outline=outline, width=width)
    draw.rectangle([x1, y1+r, x2, y2-r], fill=fill, outline=outline, width=width)

def draw_arrowhead(draw, x, y, angle, color=DARK):
    import math
    size = 10
    p1 = (x + size * math.cos(math.radians(angle+30)), y + size * math.sin(math.radians(angle+30)))
    p2 = (x + size * math.cos(math.radians(angle-30)), y + size * math.sin(math.radians(angle-30)))
    draw.polygon([(x, y), p1, p2], fill=color)

def draw_arrow(draw, x1, y1, x2, y2, color=DARK, width=2):
    import math
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
    angle = math.degrees(math.atan2(y2-y1, x2-x1))
    draw_arrowhead(draw, x2, y2, angle, color)

# ============ DFD LEVEL 0 ============
def draw_dfd_level0():
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)
    f12 = get_font(12)
    f14 = get_font(14)
    f16 = get_font(16)
    f18 = get_font(18)
    f20 = get_font(20)

    # Title
    draw.text((W//2, 25), "Data Flow Diagram - Level 0 (Context Diagram)", fill=DARK, font=f18, anchor="mt")
    draw.text((W//2, 50), "ICC Companion System", fill=GRAY, font=f14, anchor="mt")

    # Student entity (left)
    sx, sy = 80, 250
    sw, sh = 200, 140
    rounded_rect(draw, [sx, sy, sx+sw, sy+sh], 20, LGRAY, BLUE, 3)
    draw.text((sx+sw//2, sy+40), "👤", fill=DARK, font=f20, anchor="mt")
    draw.text((sx+sw//2, sy+70), "STUDENT", fill=DARK, font=f16, anchor="mt")
    draw.text((sx+sw//2, sy+95), "(External Entity)", fill=GRAY, font=f12, anchor="mt")

    # Admin entity (right)
    ax, ay = 720, 250
    aw, ah = 200, 140
    rounded_rect(draw, [ax, ay, ax+aw, ay+ah], 20, LGRAY, ORANGE, 3)
    draw.text((ax+aw//2, ay+40), "🔐", fill=DARK, font=f20, anchor="mt")
    draw.text((ax+aw//2, ay+70), "ADMIN", fill=DARK, font=f16, anchor="mt")
    draw.text((ax+aw//2, ay+95), "(External Entity)", fill=GRAY, font=f12, anchor="mt")

    # Main process (center)
    px, py = 350, 220
    pw, ph = 300, 200
    rounded_rect(draw, [px, py, px+pw, py+ph], 20, (219, 234, 254), BLUE, 3)
    draw.text((px+pw//2, py+45), "ICC COMPANION", fill=BLUE, font=f18, anchor="mt")
    draw.text((px+pw//2, py+75), "Campus Portal System", fill=DARK, font=f16, anchor="mt")
    draw.line([(px+40, py+95), (px+pw-40, py+95)], fill=GRAY, width=1)
    draw.text((px+pw//2, py+115), "📊 Attendance Tracker", fill=DARK, font=f12, anchor="mt")
    draw.text((px+pw//2, py+135), "📅 Exam Timetable", fill=DARK, font=f12, anchor="mt")
    draw.text((px+pw//2, py+155), "📢 Announcements", fill=DARK, font=f12, anchor="mt")
    draw.text((px+pw//2, py+175), "🔍 Lost & Found", fill=DARK, font=f12, anchor="mt")

    # Database (bottom center)
    dbx, dby = 400, 510
    dbw, dbh = 200, 90
    rounded_rect(draw, [dbx, dby, dbx+dbw, dby+dbh], 15, (220, 252, 231), GREEN, 3)
    draw.text((dbx+dbw//2, dby+25), "🗄️", fill=DARK, font=f20, anchor="mt")
    draw.text((dbx+dbw//2, dby+55), "MySQL Database", fill=DARK, font=f14, anchor="mt")
    draw.text((dbx+dbw//2, dby+75), "campus_portal", fill=GRAY, font=f12, anchor="mt")

    # Arrows: Student <-> System
    draw_arrow(draw, sx+sw, sy+sh//2, px, py+ph//2)  # Student -> System
    draw_arrow(draw, px+pw, py+ph//2, ax, ay+ah//2)  # System -> Admin (actually Admin -> System direction)

    # Redraw arrowheads in correct direction
    # Student -> System (left to center)
    draw_arrow(draw, sx+sw, sy+sh//2, px, py+ph//2, width=2)
    # System -> Student (center to left) - reverse
    draw_arrow(draw, px, py+ph//2, sx+sw, sy+sh//2, width=2)
    # Admin -> System (right to center)
    draw_arrow(draw, ax, ay+ah//2, px+pw, py+ph//2, width=2)
    # System -> Admin (center to right)
    draw_arrow(draw, px+pw, py+ph//2, ax, ay+ah//2, width=2)

    # Labels on arrows
    draw.text((220, 270), "Login / View Data", fill=DARK, font=f12, anchor="mt")
    draw.text((220, 350), "Attendance, Exams,", fill=DARK, font=f12, anchor="mt")
    draw.text((220, 368), "Announcements...", fill=DARK, font=f12, anchor="mt")

    draw.text((690, 280), "Manage Records", fill=DARK, font=f12, anchor="mt")
    draw.text((690, 350), "Post Announcements,", fill=DARK, font=f12, anchor="mt")
    draw.text((690, 368), "Mark Attendance...", fill=DARK, font=f12, anchor="mt")

    # System <-> DB
    draw_arrow(draw, px+pw//2, py+ph, dbx+dbw//2, dby, width=2)
    draw_arrow(draw, dbx+dbw//2, dby, px+pw//2, py+ph, width=2)
    draw.text((px+pw//2, py+ph+20), "CRUD Operations", fill=GRAY, font=f12, anchor="mt")

    # Legend
    draw.text((W//2, H-40), "Figure 6.2 \u2014 DFD Level 0: ICC Companion Context Diagram", fill=GRAY, font=f12, anchor="mt")

    return img

# ============ DFD LEVEL 1 ============
def draw_dfd_level1():
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)
    f11 = get_font(11)
    f12 = get_font(12)
    f14 = get_font(14)
    f16 = get_font(16)

    draw.text((W//2, 20), "Data Flow Diagram - Level 1", fill=DARK, font=f16, anchor="mt")

    # Student entity (left)
    sx, sy = 30, 270
    sw, sh = 130, 100
    rounded_rect(draw, [sx, sy, sx+sw, sy+sh], 15, LGRAY, BLUE, 3)
    draw.text((sx+sw//2, sy+30), "👤 Student", fill=DARK, font=f14, anchor="mt")

    # Admin entity (right) 
    ax, ay = 840, 270
    aw, ah = 130, 100
    rounded_rect(draw, [ax, ay, ax+aw, ay+ah], 15, LGRAY, ORANGE, 3)
    draw.text((ax+aw//2, ay+30), "🔐 Admin", fill=DARK, font=f14, anchor="mt")

    # Process boxes (center)
    processes = [
        ("1.0\nStudent\nLogin", 200, 80, BLUE),
        ("2.0\nAttendance\nViewing", 370, 80, (37, 99, 235)),
        ("3.0\nExam\nTimetable", 540, 80, (37, 99, 235)),
        ("4.0\nLost & Found\nBrowse", 710, 80, (37, 99, 235)),
        ("5.0\nAnnouncement\nDisplay", 200, 280, (37, 99, 235)),
        ("6.0\nResource\nManagement", 370, 280, (37, 99, 235)),
        ("7.0\nStudent\nCRUD", 540, 280, (37, 99, 235)),
        ("8.0\nAttendance\nMarking", 710, 280, (37, 99, 235)),
    ]

    for i, (label, px, py, color) in enumerate(processes):
        lines = label.split('\n')
        pw, ph = 140, 90
        rounded_rect(draw, [px, py, px+pw, py+ph], 10, (238, 242, 255), color, 2)
        yoff = 20
        for ln in lines:
            if ln[0].isdigit():
                draw.text((px+pw//2, py+yoff), ln, fill=color, font=f12, anchor="mt")
            else:
                draw.text((px+pw//2, py+yoff), ln, fill=DARK, font=f11, anchor="mt")
            yoff += 18

    # DB store
    dbx, dby = 370, 520
    dbw, dbh = 260, 70
    rounded_rect(draw, [dbx, dby, dbx+dbw, dby+dbh], 12, (220, 252, 231), GREEN, 3)
    draw.text((dbx+dbw//2, dby+20), "🗄️ Campus Portal Database", fill=DARK, font=f14, anchor="mt")
    draw.text((dbx+dbw//2, dby+45), "(12 Tables)", fill=GRAY, font=f12, anchor="mt")

    # Student -> Processes
    for _, px, py, _ in processes:
        draw_arrow(draw, sx+sw, sy+sh//2, px+pw//2, py, width=1)
        draw_arrow(draw, px+pw//2, py+ph, sx+sw, sy+sh//2, width=1)

    # Admin -> Processes
    for _, px, py, _ in processes:
        draw_arrow(draw, ax, ay+ah//2, px+pw, py+ph//2, width=1)

    # Processes -> DB
    procs = [(200, 80), (370, 80), (540, 80), (710, 80), (200, 280), (370, 280), (540, 280), (710, 280)]
    for px, py in procs:
        draw_arrow(draw, px+70, py+90, dbx+dbw//2, dby, width=1)
        draw_arrow(draw, dbx+dbw//2, dby+dbh, px+70, py+90, width=1)

    draw.text((W//2, 620), "Figure 6.3 \u2014 DFD Level 1: Detailed Process Flow", fill=GRAY, font=f12, anchor="mt")

    return img

# ============ ER DIAGRAM ============
def draw_er_diagram():
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)
    f11 = get_font(11)
    f12 = get_font(12)
    f14 = get_font(14)
    f16 = get_font(16)

    draw.text((W//2, 18), "Entity-Relationship (ER) Diagram", fill=DARK, font=f16, anchor="mt")
    draw.text((W//2, 40), "ICC Companion - Database Schema", fill=GRAY, font=f14, anchor="mt")

    entities = [
        # (name, cx, cy, w, h, color, attrs)
        ("departments", 150, 130, 170, 80, (59, 130, 246),
         ["dept_id (PK)", "dept_code (U)", "dept_name", "max_semesters"]),
        ("students", 500, 130, 170, 80, (16, 185, 129),
         ["student_id (PK)", "roll_number (U)", "name", "dob", "dept_code (FK)", "semester"]),
        ("subjects", 850, 130, 170, 80, (245, 158, 11),
         ["subject_id (PK)", "subject_code", "subject_name", "dept_code (FK)", "semester"]),
        ("attendance", 350, 340, 170, 80, (239, 68, 68),
         ["attendance_id (PK)", "roll_number (FK)", "subject_id (FK)", "attendance_date", "status"]),
        ("exams", 650, 340, 170, 80, (168, 85, 247),
         ["exam_id (PK)", "subject_id (FK)", "exam_date", "start_time", "end_time", "room", "exam_type"]),
        ("announcements", 140, 540, 170, 80, (236, 72, 153),
         ["announcement_id (PK)", "title", "priority", "target_dept", "target_sem"]),
        ("lost_found", 460, 540, 170, 80, (14, 165, 233),
         ["item_id (PK)", "title", "item_type", "category", "status", "location"]),
        ("class_routines", 780, 540, 170, 80, (132, 204, 22),
         ["routine_id (PK)", "title", "file_url", "dept_code (FK)", "semester"]),
    ]

    # Draw entities
    for name, cx, cy, w, h, color, attrs in entities:
        # Entity box
        rounded_rect(draw, [cx-w//2, cy-25, cx+w//2, cy+25], 8, LGRAY, color, 2)
        draw.text((cx, cy), name, fill=color, font=f14, anchor="mt")

        # Attributes below
        yoff = cy + 35
        for attr in attrs:
            draw.text((cx, yoff), attr, fill=DARK, font=f11, anchor="mt")
            yoff += 16

    # Draw relationships
    # dept -> students (1:M)
    draw_arrow(draw, 240, 170, 410, 170, GRAY, 1)
    draw.text((325, 158), "1", fill=BLUE, font=f12, anchor="mt")
    draw.text((325, 178), "M", fill=GREEN, font=f12, anchor="mt")
    draw.text((325, 195), "has", fill=GRAY, font=f11, anchor="mt")

    # dept -> subjects (1:M)
    draw_arrow(draw, 240, 130, 760, 130, GRAY, 1)
    draw.text((500, 118), "1", fill=BLUE, font=f12, anchor="mt")
    draw.text((500, 138), "M", fill=ORANGE, font=f12, anchor="mt")
    draw.text((500, 155), "offers", fill=GRAY, font=f11, anchor="mt")

    # student -> attendance (1:M)
    draw_arrow(draw, 500, 210, 430, 300, GRAY, 1)
    draw.text((510, 240), "1", fill=BLUE, font=f12, anchor="mt")
    draw.text((430, 240), "M", fill=RED, font=f12, anchor="mt")
    draw.text((470, 258), "records", fill=GRAY, font=f11, anchor="mt")

    # subject -> attendance (1:M)
    draw_arrow(draw, 680, 180, 600, 300, GRAY, 1)
    draw.text((670, 230), "1", fill=BLUE, font=f12, anchor="mt")
    draw.text((600, 230), "M", fill=RED, font=f12, anchor="mt")

    # subject -> exams (1:M)
    draw_arrow(draw, 780, 200, 720, 300, GRAY, 1)
    draw.text((780, 240), "1", fill=BLUE, font=f12, anchor="mt")
    draw.text((720, 240), "M", fill=PURPLE if 'PURPLE' in dir() else (168,85,247), font=f12, anchor="mt")

    # dept -> class_routines (1:M)
    draw_arrow(draw, 240, 130, 700, 500, GRAY, 1)
    draw.text((420, 430), "1", fill=BLUE, font=f12, anchor="mt")
    draw.text((440, 450), "M", fill=(132,204,22), font=f12, anchor="mt")

    draw.text((W//2, 650), "Figure 6.5 \u2014 Entity-Relationship (ER) Diagram", fill=GRAY, font=f12, anchor="mt")

    return img

# Save diagrams
out_dir = r'C:\xampp\htdocs\ICC_Companion\temp\ppt_and_report\my_report'
os.makedirs(out_dir, exist_ok=True)

dfd0 = draw_dfd_level0()
dfd0.save(os.path.join(out_dir, 'dfd_level0.png'))
print(f"DFD Level 0 saved: {dfd0.size}")

dfd1 = draw_dfd_level1()
dfd1.save(os.path.join(out_dir, 'dfd_level1.png'))
print(f"DFD Level 1 saved: {dfd1.size}")

er = draw_er_diagram()
er.save(os.path.join(out_dir, 'er_diagram.png'))
print(f"ER Diagram saved: {er.size}")

print("\nAll diagrams generated successfully!")
