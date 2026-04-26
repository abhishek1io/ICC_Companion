// =============================================
// ICC COMPANION - MAIN JAVASCRIPT
// ICON COMMERCE COLLEGE (ICC)
// =============================================

// Base URL for API calls
var API_BASE = 'api/';

// =============================================
// SESSION MANAGEMENT
// =============================================

// Check if student is logged in
function checkStudentLogin() {
    var roll = sessionStorage.getItem('studentRoll');
    if (!roll) {
        window.location.href = '../student-login.html';
        return false;
    }
    return true;
}

// Check if admin is logged in
function checkAdminLogin() {
    var adminId = sessionStorage.getItem('adminId');
    if (!adminId) {
        window.location.href = '../admin-login.html';
        return false;
    }
    return true;
}

// Logout function
function logout(type) {
    sessionStorage.clear();
    if (type === 'student') {
        window.location.href = '../student-login.html';
    } else {
        window.location.href = '../admin-login.html';
    }
}

// Get student info from session
function getStudentInfo() {
    return {
        roll: sessionStorage.getItem('studentRoll'),
        name: sessionStorage.getItem('studentName'),
        dept: sessionStorage.getItem('studentDept'),
        semester: sessionStorage.getItem('studentSemester')
    };
}

// Get admin info from session
function getAdminInfo() {
    return {
        id: sessionStorage.getItem('adminId'),
        name: sessionStorage.getItem('adminName'),
        role: sessionStorage.getItem('adminRole'),
        assignedDept: sessionStorage.getItem('assignedDept') || 'all',
        assignedSemester: sessionStorage.getItem('assignedSemester') || 'all'
    };
}

// =============================================
// API HELPER FUNCTIONS
// =============================================

// Make GET request
function apiGet(endpoint, callback) {
    fetch(API_BASE + endpoint)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            callback(null, data);
        })
        .catch(function (error) {
            callback(error, null);
        });
}

// Make POST request
function apiPost(endpoint, formData, callback) {
    fetch(API_BASE + endpoint, {
        method: 'POST',
        body: formData
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            callback(null, data);
        })
        .catch(function (error) {
            callback(error, null);
        });
}

// =============================================
// UI HELPER FUNCTIONS
// =============================================

// Show loading indicator
function showLoading(elementId) {
    var element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = '<div style="text-align: center; padding: 40px; color: #64748b;">Loading...</div>';
    }
}

// Show alert message
function showAlert(message, type) {
    var alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-' + type;
    alertDiv.textContent = message;

    var container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);

        // Auto remove after 5 seconds
        setTimeout(function () {
            alertDiv.remove();
        }, 5000);
    }
}

// Format date for display
function formatDate(dateString) {
    var date = new Date(dateString);
    var options = { year: 'numeric', month: 'short', day: 'numeric' };
    return date.toLocaleDateString('en-IN', options);
}

// Calculate days remaining
function daysRemaining(dateString) {
    var today = new Date();
    today.setHours(0, 0, 0, 0);
    var target = new Date(dateString);
    var diff = target - today;
    var days = Math.ceil(diff / (1000 * 60 * 60 * 24));
    return days;
}

// Get attendance status class
function getAttendanceStatus(percentage) {
    if (percentage >= 75) {
        return { class: 'green', text: 'Safe', badge: 'badge-success' };
    } else if (percentage >= 65) {
        return { class: 'orange', text: 'Warning', badge: 'badge-warning' };
    } else {
        return { class: 'red', text: 'Shortage', badge: 'badge-danger' };
    }
}

// Calculate classes that can be missed
function classesCanMiss(present, total, required) {
    required = required || 75;
    // Formula: present / (total + x) >= required/100
    // x = (present * 100 / required) - total
    var maxTotal = Math.floor((present * 100) / required);
    var canMiss = maxTotal - total;
    return canMiss > 0 ? canMiss : 0;
}

// =============================================
// RESTRICTION ENFORCEMENT
// =============================================

// Lock filters for assigned staff
function applyRestrictions(deptSelectorId, semSelectorId) {
    var admin = getAdminInfo();
    if (admin.role === 'super-admin') return; // Super admins have full access

    if (admin.assignedDept !== 'all') {
        var deptEl = document.getElementById(deptSelectorId);
        if (deptEl) {
            deptEl.value = admin.assignedDept;
            deptEl.disabled = true;
            deptEl.style.backgroundColor = '#f1f5f9';
            deptEl.style.cursor = 'not-allowed';
            
            // Trigger change event to load data
            var event = new Event('change');
            deptEl.dispatchEvent(event);
        }
    }

    if (admin.assignedSemester !== 'all') {
        var semEl = document.getElementById(semSelectorId);
        if (semEl) {
            semEl.value = admin.assignedSemester;
            semEl.disabled = true;
            semEl.style.backgroundColor = '#f1f5f9';
            semEl.style.cursor = 'not-allowed';
            
            // Trigger change event to load data
            var event = new Event('change');
            semEl.dispatchEvent(event);
        }
    }
}

// Set user info in header with role and scope
function updateHeaderUI() {
    var admin = getAdminInfo();
    var nameEl = document.getElementById('adminName');
    if (nameEl) {
        var roleText = admin.role === 'super-admin' ? 'Principal / HOD' : 'Faculty';
        var scopeText = '';
        if (admin.role !== 'super-admin') {
            scopeText = ' (' + (admin.assignedDept === 'all' ? 'All Depts' : admin.assignedDept);
            scopeText += ' - ' + (admin.assignedSemester === 'all' ? 'All Sem' : 'Sem ' + admin.assignedSemester) + ')';
        }
        nameEl.innerHTML = admin.name + ' <small style="color: #94a3b8; font-weight: normal; margin-left: 5px;">[' + roleText + scopeText + ']</small>';
    }
}

// Set user name in header
function setUserName(name, elementId) {
    var element = document.getElementById(elementId || 'userName');
    if (element) {
        element.textContent = name;
    }
}

// Mark active navigation link
function setActiveNav(page) {
    var links = document.querySelectorAll('.nav-menu a');
    links.forEach(function (link) {
        link.classList.remove('active');
        if (link.getAttribute('href').includes(page)) {
            link.classList.add('active');
        }
    });
}

// Populate department dropdowns dynamically
function populateDepartments(selectorId, callback) {
    var selector = document.getElementById(selectorId);
    if (!selector) return;

    fetch('../api/get-departments.php')
        .then(function(res) { return res.json(); })
        .then(function(data) {
            if (data.success) {
                var currentVal = selector.value;
                var html = selector.getAttribute('data-allow-all') === 'true' ? '<option value="all">All Departments</option>' : '<option value="">Select Dept</option>';
                data.data.forEach(function(dept) {
                    html += '<option value="' + dept.dept_code + '" data-max-sem="' + dept.max_semesters + '">' + dept.dept_name + ' (' + dept.dept_code + ')</option>';
                });
                selector.innerHTML = html;
                if (currentVal) selector.value = currentVal;
                if (callback) callback(data.data);
            }
        });
}

// Update semester dropdown based on selected department's max semesters
function updateSemesterDropdown(deptSelectorId, semSelectorId) {
    var deptEl = document.getElementById(deptSelectorId);
    var semEl = document.getElementById(semSelectorId);
    if (!deptEl || !semEl) return;

    var selectedOption = deptEl.options[deptEl.selectedIndex];
    var maxSem = selectedOption ? parseInt(selectedOption.getAttribute('data-max-sem')) : 6;
    if (deptEl.value === 'all' || !deptEl.value) maxSem = 8; // Default fallback

    var html = semEl.getAttribute('data-allow-all') === 'true' ? '<option value="all">All Semesters</option>' : '<option value="">Select Sem</option>';
    for (var i = 1; i <= maxSem; i++) {
        html += '<option value="' + i + '">' + i + '</option>';
    }
    semEl.innerHTML = html;
}

