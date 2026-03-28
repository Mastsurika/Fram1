# Farm Management System - Quick Start Guide

## Overview

Welcome to the Farm Management System! This is a comprehensive web application designed to help you manage vegetable farming operations efficiently.

## System Requirements

- Windows, Mac, or Linux operating system
- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Edge, Safari)
- Internet connection (for initial setup)

## Installation & Running

### Option 1: Windows Users (Easiest)

1. Double-click `run.bat` in the project folder
2. A command window will open and automatically:
   - Create a Python virtual environment
   - Install required packages
   - Start the application
3. Open your browser and go to: **http://localhost:5000**
4. Create an account and start using!

### Option 2: Mac/Linux Users

1. Open Terminal and navigate to the project folder
2. Run: `bash run.sh`
3. Follow the same steps as Windows users

### Option 3: Manual Setup (All Systems)

1. Open Command Prompt/Terminal
2. Navigate to project folder: `cd path/to/fram1`
3. Create virtual environment: `python -m venv venv`
4. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install packages: `pip install -r requirements.txt`
6. Run app: `python app.py`
7. Open browser: **http://localhost:5000**

## First Time Use

### Step 1: Create Account
- Click "Register" on login page
- Enter username, email, and password
- Click "Register"
- You'll be redirected to login page
- Log in with your credentials

### Step 2: Create Your First Field
- Click "Crops" in the navigation menu
- Click "+ Add New Field"
- Enter field name (e.g., "North Field")
- Enter field area in square meters
- Enter location
- Click "Create Field"

### Step 3: Add a Crop
- Find your field in the list
- Click "Add Crop Round"
- Enter crop name (e.g., "Tomato", "Lettuce")
- Select planting date
- Select estimated harvest date
- Enter quantity planted in kg
- Add optional notes
- Click "Save Crop Round"

### Step 4: Log Activities
- Click on a crop to view details
- Scroll to "Add New Activity" section
- Select activity type (watering, fertilizing, etc.)
- Add description and quantity
- Click "Add Activity"

### Step 5: Record Harvest
- View crop details
- Enter quantity harvested and price per unit
- Click "Mark as Harvested"
- Item automatically added to inventory

## Key Features to Explore

### 📊 Dashboard
- See all your statistics at a glance
- View active crops and alerts
- Check recent activities
- Get quick access to main features

### 🌾 Crop Management
- Manage multiple fields
- Track multiple crop rounds per field
- Monitor crop status and timeline

### ⚠️ Alerts
- Get notified when crops are ready for harvest
- Monitor inventory expiry dates
- Stay on top of farm operations

### 📋 Activity Log
- Complete history of all farm activities
- Filter by date and activity type
- Track what was done and when

### 📦 Inventory
- Manage harvested products
- Track quantities and values
- Update item status (in stock, sold, expired)

### 📈 Reports
- Production statistics and summaries
- Inventory valuation
- Harvest history by crop type

## Common Tasks

### How to update crop status?
- The status updates automatically based on crop progress
- View crop details to see current status
- Mark as harvested through the crop details page

### How to check alerts?
- Click "Alerts" in the navigation
- See all harvest alerts and expiry notices
- Click "View & Harvest" to take action

### How to manage inventory?
- Go to Inventory page
- Update quantities by editing numbers
- Change status (In Stock, Sold, Expired)
- Click "Save" to confirm changes

### How to export reports?
- Go to Reports page
- Screenshot or print from browser (Ctrl+P)
- Consider using browser's "Save as PDF" option

## Tips for Best Results

✓ **Add activities regularly** - Track your work as you do it
✓ **Set accurate dates** - Better dates = better alerts
✓ **Update prices** - Track costs for accurate inventory valuation
✓ **Add notes** - Record special conditions or varieties
✓ **Check alerts daily** - Stay ahead of harvest schedules
✓ **Backup your data** - Keep copies of database for safety

## Troubleshooting

### Port 5000 already in use
- Another app is using port 5000
- Open `app.py` and change `port=5000` to `port=5001`
- Save and run again

### "Module not found" error
- Python packages not installed
- Run: `pip install -r requirements.txt` again
- Make sure virtual environment is activated

### Database errors
- Delete `farm_management.db` file (it will be recreated)
- Run the app again
- Your old data will be lost, so be careful!

### Application won't start
- Close any other Python scripts
- Make sure port 5000 is not blocked by firewall
- Try using a different port (see above)

## Keyboard Shortcuts

- `Ctrl+P` - Print current page
- `Ctrl+L` - Go to address bar
- `F12` - Open browser developer tools (advanced users)

## File Structure Explained

```
fram1/
└─ app.py              Main application (Python)
└─ run.bat             Windows startup script
└─ run.sh              Mac/Linux startup script
└─ requirements.txt    Python packages needed
└─ README.md          Detailed documentation
└─ templates/         HTML pages (website content)
└─ static/            CSS & styling
└─ farm_management.db Database (created after first run)
```

## Security Note

This is a local application for personal farm management. 

**For sharing/hosting:**
- Change the SECRET_KEY in app.py
- Use HTTPS
- Add proper user authentication
- Consider deploying on a server

## Getting Help

1. Check README.md for detailed information
2. Review code comments in app.py
3. Check template files for feature details

## Next Steps

1. ✓ Set up the application (you just did this!)
2. ✓ Create your account
3. Create your first field
4. Add your first crop
5. Start logging activities
6. Record your first harvest
7. Check reports and analytics

---

**Enjoy managing your farm with the Farm Management System!** 🌱

For more details, see README.md
