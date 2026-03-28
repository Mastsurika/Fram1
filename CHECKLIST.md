# ✅ Farm Management System - Installation & Verification Checklist

## Pre-Installation Checklist

- [ ] Python 3.7+ is installed on your computer
  - Verify: Open Command Prompt/Terminal and type: `python --version`
  - Should show: Python 3.x.x (where x represents version numbers)
  
- [ ] Internet connection is available (for first-time setup)

- [ ] Port 5000 is available on your computer
  - (Or you're willing to change it in CONFIGURATION.md)

---

## Installation Steps

### Windows Users

- [ ] Step 1: Navigate to the project folder
  - Open File Explorer
  - Go to: C:\Users\Bew\Desktop\fram1

- [ ] Step 2: Run the startup script
  - Find file: `run.bat`
  - Double-click it
  - A command window will open

- [ ] Step 3: Wait for installation
  - System will create virtual environment (might take 1-2 minutes)
  - System will install packages (might take 2-3 minutes)
  - Look for message: "The application will be available at..."

- [ ] Step 4: Open browser
  - Go to: http://localhost:5000
  - Should see login page

### Mac/Linux Users

- [ ] Step 1: Open Terminal
  - Find Terminal application
  - Or: Press Ctrl+Alt+T (Ubuntu)

- [ ] Step 2: Navigate to project
  ```bash
  cd /Users/Bew/Desktop/fram1
  ```
  (Adjust path if different)

- [ ] Step 3: Run startup script
  ```bash
  bash run.sh
  ```

- [ ] Step 4: Open browser
  - Go to: http://localhost:5000
  - Should see login page

### Manual Installation (All Systems)

- [ ] Step 1: Open Terminal/Command Prompt
  - Windows: Win+R, type `cmd`, press Enter
  - Mac/Linux: Open Terminal application

- [ ] Step 2: Navigate to folder
  ```
  cd c:\Users\Bew\Desktop\fram1
  ```

- [ ] Step 3: Create virtual environment
  ```
  python -m venv venv
  ```

- [ ] Step 4: Activate virtual environment
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
  - Prompt should show: `(venv)` at the start

- [ ] Step 5: Install packages
  ```
  pip install -r requirements.txt
  ```

- [ ] Step 6: Run application
  ```
  python app.py
  ```

- [ ] Step 7: Open browser
  - Go to: http://localhost:5000

---

## First-Time Setup Checklist

### Create Your Account

- [ ] See login page at http://localhost:5000
- [ ] Click "Register here" link
- [ ] Enter desired username (e.g., `farmermanuel`)
- [ ] Enter your email address
- [ ] Enter a password (8+ characters recommended)
- [ ] Confirm password
- [ ] Click "Register" button
- [ ] See success message
- [ ] Redirected back to login page

### Login to System

- [ ] Enter your username
- [ ] Enter your password
- [ ] Click "Login" button
- [ ] See dashboard page

### Dashboard Orientation

- [ ] Can see: Welcome message with your username
- [ ] Can see: 4 stat cards (Fields, Crops, Inventory, Value)
- [ ] Can see: Navigation menu at top (Dashboard, Crops, Alerts, etc.)
- [ ] Can see: Quick actions section

---

## Creating Your First Farm

### Step 1: Create a Field

- [ ] Click "Crops" in navigation menu
- [ ] See fields area (empty first time)
- [ ] Click "+ Add New Field" button
- [ ] Enter field name (e.g., "Main Garden")
- [ ] Enter field area in m² (e.g., 1000)
- [ ] Enter location (e.g., "Farm North Section")
- [ ] Click "Create Field" button
- [ ] See field created in list

### Step 2: Add a Crop

- [ ] Find your field in the list
- [ ] Click "Add Crop Round" button
- [ ] Enter crop name (e.g., "Tomato")
- [ ] Select planting date (today or past)
- [ ] Select harvest date (60+ days from now)
- [ ] Enter quantity planted (e.g., 50 kg)
- [ ] Enter optional notes
- [ ] Click "Save Crop Round"
- [ ] Redirected back to crops page

### Step 3: View Your Crop

- [ ] Find your field's crop in the table
- [ ] Click "View" button
- [ ] See crop details page
- [ ] Can see all crop information
- [ ] Can see empty activity log

### Step 4: Add an Activity

- [ ] On crop details page, find "Add New Activity" section
- [ ] Select activity type (e.g., "Watering")
- [ ] Enter description (e.g., "Morning watering")
- [ ] Enter quantity (e.g., 50)
- [ ] Select unit (e.g., "liters")
- [ ] Click "Add Activity" button
- [ ] Activity appears in the log below
- [ ] Activity date is auto-recorded

---

## Checking Key Features

### Dashboard

- [ ] Go to "Dashboard" menu
- [ ] Can see summary statistics
- [ ] Can see recent activities
- [ ] Can see active alerts (if any)

### Alerts

- [ ] Click "Alerts" in menu
- [ ] Should see either:
  - Harvest alerts (crops ready within 7 days)
  - Or: "No crops ready for harvest" message
  - Or: "No inventory expiry alerts" message

### Activity Log

- [ ] Click "Activities" in menu
- [ ] Should see your logged activity
- [ ] Shows date, type, description, quantities

### Inventory

- [ ] Click "Inventory" in menu
- [ ] Currently should be empty (no harvests yet)
- [ ] Check will look like this after first harvest:
  - Product name, quantity, price, total value

### Reports

- [ ] Click "Reports" in menu
- [ ] See production statistics
- [ ] See inventory summary (empty for now)

---

## Testing Complete Workflow

### Record a Harvest

- [ ] Go to Crops → View your crop
- [ ] Scroll to "Actions" section
- [ ] Enter quantity harvested (e.g., 400)
- [ ] Enter price per unit ($) (e.g., 2.50)
- [ ] Click "Mark as Harvested"
- [ ] Crop status changes to "Harvested"

### Check Inventory Update

- [ ] Go to "Inventory" menu
- [ ] Should see your harvested product
- [ ] Shows quantity, unit price, total value
- [ ] Click "Save" to confirm changes

### Check Harvest Report

- [ ] Go to "Reports" menu
- [ ] Should see harvested crop in table
- [ ] Shows all production details
- [ ] Calculates total inventory value

---

## Verification Tests

### Performance

- [ ] Pages load in < 2 seconds
- [ ] Can add crop without delays
- [ ] Can log activities quickly
- [ ] Can access all pages

### Data Persistence

- [ ] Logout (click username → Logout)
- [ ] Login again
- [ ] All data still there
- [ ] No data was lost

### Navigation

- [ ] Can go to Dashboard from any page
- [ ] Each navigation item works
- [ ] Back button works properly
- [ ] Can access all features

### Responsive Design

- [ ] Website looks good on current screen size
- [ ] Try resizing browser window
- [ ] Layout should adjust (responsive)
- [ ] All buttons remain clickable

---

## Database Verification

### Check Database File

- [ ] Open project folder
- [ ] Should see file: `farm_management.db`
- [ ] File size: 50-200 KB (normal size)
- [ ] File created after first run

### Verify Data Saved

- [ ] Stop the application (Ctrl+C in terminal)
- [ ] Go back to browser
- [ ] Should see "Connection refused" error (normal)
- [ ] Start app again (`python app.py`)
- [ ] Go back to login
- [ ] Login and verify all data still there

---

## Common Checks

### If Port Already Used

- [ ] See error: "Address already in use"
- [ ] Fix: Edit app.py, change port 5000 to 5001
- [ ] Or: Find what's using port 5000 and close it

### If Python Not Found

- [ ] See: "python: command not found" or "'python' is not recognized"
- [ ] Fix: Install Python 3.7+ from python.org
- [ ] Make sure "Add Python to PATH" is checked

### If pip Install Fails

- [ ] See: Permission or network errors
- [ ] Fix: Run as Administrator (Windows)
- [ ] Or: Check internet connection
- [ ] Try again: `pip install -r requirements.txt`

### If Page Won't Load

- [ ] Check correct URL: http://localhost:5000
- [ ] Check if terminal shows any errors
- [ ] Restart application
- [ ] Wait 5 seconds for full startup

---

## Security Verification

### Check Session Working

- [ ] Login successfully
- [ ] Navigate around the site
- [ ] Try accessing /crop-management without logout
- [ ] Page should load (logged in works)
- [ ] Logout
- [ ] Try accessing /crop-management
- [ ] Should redirect to login (security works)

### Password Hashing

- [ ] Register new account
- [ ] Intentionally use wrong password
- [ ] Should fail (login denied)
- [ ] Check database file (farm_management.db)
- [ ] Password not visible in plain text

---

## Backup & Restore Test

### Create Backup

- [ ] Stop application
- [ ] Copy `farm_management.db` file
- [ ] Rename copy: `farm_management_backup.db`
- [ ] Store safely (Desktop or USB)

### Restore Backup

- [ ] Add new data to system
- [ ] Verify new data shows up
- [ ] Stop application
- [ ] Delete `farm_management.db`
- [ ] Copy your backup and rename to `farm_management.db`
- [ ] Start application again
- [ ] Old data should be restored

---

## Documentation Checks

- [ ] Can find and read README.md
- [ ] Can find QUICK_START.md
- [ ] Documentation is clear
- [ ] Examples make sense
- [ ] Can follow instructions

---

## Final Verification Checklist

- [ ] Application starts without errors
- [ ] Can create an account
- [ ] Can login/logout
- [ ] Can create fields
- [ ] Can add crops
- [ ] Can log activities
- [ ] Can record harvests
- [ ] Can view inventory
- [ ] Can access alerts
- [ ] Can view reports
- [ ] Data persists after logout
- [ ] Database file exists
- [ ] All pages are responsive
- [ ] Navigation works properly
- [ ] No error messages on normal usage

---

## ✅ Success!

If all checks pass, you have successfully:

✓ Installed the Farm Management System
✓ Created an account
✓ Created your first field
✓ Added crops
✓ Logged activities
✓ Tested the complete workflow
✓ Verified data persistence
✓ Confirmed responsive design
✓ Tested backup functionality

**Your system is ready for use!**

---

## 📞 Next Steps

1. **Explore:** Spend time exploring all features
2. **Learn:** Read QUICK_START.md and FEATURES.md
3. **Setup:** Create multiple fields and crops
4. **Optimize:** Adjust settings in CONFIGURATION.md if needed
5. **Backup:** Set up regular database backups
6. **Use:** Start using for real farm management

---

## 🎉 Quick Command Reference

**Start Application:**
- Windows: Double-click `run.bat`
- Mac/Linux: `bash run.sh`

**Manual Start:**
```bash
# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Run app
python app.py
```

**Stop Application:**
- Press: Ctrl+C in terminal

**Access Application:**
- Browser: http://localhost:5000

**Change Port:**
- Edit: app.py
- Find: `port=5000`
- Change to: `port=5001` (or any other)

**Reset Database:**
- Delete: `farm_management.db`
- Restart app (new database created)

---

Good luck with your farm management! 🌱

*Document Version: 1.0*
*System: Farm Management System v1.0*
*Last Updated: January 2024*
