# Farm Management System

A comprehensive web application for managing vegetable farm operations, including crop tracking, activity logging, inventory management, and harvest alerts.

## Features

### 1. **User Authentication**
- User registration and login system
- Secure password hashing
- Session management

### 2. **Crop Management**
- Create and manage multiple fields
- Record crop planting details:
  - Field selection
  - Crop type
  - Planting date
  - Estimated harvest date
  - Quantity planted
  - Notes
- Track crop status (planting, growing, ready, harvested)

### 3. **Activity & Task Logging**
- Record farming activities for each crop:
  - Watering
  - Fertilizing
  - Weeding
  - Spraying
  - Pest control
  - Pruning
  - Mulching
  - Custom activities
- Track activity details with quantities and units
- View complete activity history

### 4. **Harvest Alerts**
- Real-time notifications for crops ready to harvest
- Alerts displayed on dashboard and dedicated alerts page
- Shows days until or overdue harvest
- Inventory expiry alerts

### 5. **Inventory Management**
- Automatic inventory creation when crops are harvested
- **10-day expiry system**: Items expire exactly 10 days after harvest date
- Automatic status updates: Items marked as "Expired" when expiry date passes
- Track product quantities, units, and prices
- Mark items as in stock, sold, or expired
- Calculate total inventory value
- Expiry alerts for items expiring within 7 days

### 6. **Dashboard & Reporting**
- At-a-glance statistics:
  - Total fields
  - Active crops
  - Inventory count and value
- Recent activity feed
- Harvest alerts summary
- Detailed production reports:
  - Total crops harvested
  - Total harvest quantity
  - Production history by crop
- Inventory summary with valuation

## Technology Stack

**Backend:**
- Python 3.x
- Flask (Web Framework)
- Flask-SQLAlchemy (ORM)
- SQLite (Database)

**Frontend:**
- HTML5
- CSS3 (Responsive Design)
- Vanilla JavaScript

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Navigate to project directory:**
   ```
   cd c:\Users\Bew\Desktop\fram1
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app.py
   ```

5. **Open in browser:**
   - Go to `http://localhost:5000`
   - Default address: `http://127.0.0.1:5000`

## Usage Guide

### First Time Setup
1. Click "Register" to create a new account
2. Enter username, email, and password
3. Click "Register" to create your account
4. Log in with your credentials

### Getting Started
1. **Create Fields:**
   - Go to Crop Management
   - Click "Add New Field"
   - Enter field name, area, and location
   - Save

2. **Add Crop Rounds:**
   - Select a field
   - Click "Add Crop Round"
   - Enter crop details (name, dates, quantity)
   - Save

3. **Log Activities:**
   - View crop details
   - Add activities (watering, fertilizing, etc.)
   - Track quantity used and units

4. **Record Harvest:**
   - View crop details
   - Click "Mark as Harvested"
   - Enter harvest quantity and price per unit
   - Item automatically added to inventory

5. **Monitor Inventory:**
   - Go to Inventory
   - View all products
   - Update quantities or mark as sold/expired
   - Check total inventory value

6. **View Reports:**
   - Go to Reports page
   - See production statistics
   - View crop history
   - Review inventory summary

7. **Check Alerts:**
   - View alerts for crops ready to harvest
   - Check inventory expiry dates
   - Stay on top of farm operations

## Database Schema

### Tables
- **User**: User accounts and credentials
- **CropField**: Farm fields managed by users
- **CropRound**: Planting records for each crop
- **Activity**: Farming activities and tasks
- **Inventory**: Harvested products and stock

## File Structure

```
fram1/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── crop_management.html
│   ├── add_field.html
│   ├── add_crop_round.html
│   ├── view_crop.html
│   ├── alerts.html
│   ├── activity_log.html
│   ├── inventory.html
│   └── reports.html
├── static/                 # Static files
│   └── styles.css
└── farm_management.db      # SQLite database (created on first run)
```

## Security Notes

⚠️ **For Production Use:**
- Change `SECRET_KEY` in app.py to a strong, random value
- Disable `debug=True` in production
- Use environment variables for sensitive data
- Implement HTTPS
- Add input validation and sanitization
- Consider using a production WSGI server (Gunicorn, uWSGI)

## 🚀 Deployment Guide

### Option 1: Heroku (Recommended)

1. **Install Heroku CLI** and create account at heroku.com

2. **Prepare for deployment:**
   ```bash
   # Files needed for Heroku:
   # - Procfile (created)
   # - runtime.txt (created)
   # - requirements.txt (updated)
   ```

3. **Deploy to Heroku:**
   ```bash
   # Create Heroku app
   heroku create your-farm-app-name

   # Set environment variables
   heroku config:set SECRET_KEY=your-super-secret-key-here

   # Add PostgreSQL database (recommended for production)
   heroku addons:create heroku-postgresql:hobby-dev

   # Deploy
   git add .
   git commit -m "Ready for production deployment"
   git push heroku main

   # Open your app
   heroku open
   ```

### Option 2: PythonAnywhere

1. Sign up at pythonanywhere.com
2. Upload all files to PythonAnywhere
3. Set up a Flask web app
4. Configure environment variables
5. Set up your domain

### Option 3: VPS (DigitalOcean, AWS, etc.)

1. Create a VPS instance
2. Install Python, Nginx, and PostgreSQL
3. Clone your repository
4. Set up Gunicorn and Supervisor
5. Configure Nginx as reverse proxy
6. Set up SSL certificate

### Environment Variables

Create a `.env` file in production:

```bash
SECRET_KEY=your-very-secure-secret-key-here
DATABASE_URL=postgresql://user:password@host:port/database_name
# Or for SQLite (development only):
# DATABASE_URL=sqlite:///farm_management.db
```

## 🧪 Testing

Run the test suite:
```bash
python test_inventory.py
python test_template.py
python test_expiry.py
```

## Features in Detail

### Crop Status Tracking
- **Planting**: Initial planting phase
- **Growing**: Active growth period
- **Ready**: Ready for harvest (usually when estimated harvest date is within 7 days)
- **Harvested**: Crop has been harvested and stored in inventory

### Activity Types
- Watering
- Fertilizing
- Weeding
- Spraying
- Pruning
- Pest Control
- Mulching
- Custom activities

### Inventory Status
- **In Stock**: Available for sale
- **Sold**: Already sold
- **Expired**: Past expiry date

## Tips for Effective Use

1. **Regular Updates**: Add activities regularly to maintain accurate record
2. **Accurate Dates**: Use precise planting and estimated harvest dates for better alerts
3. **Price Tracking**: Update prices per unit for accurate inventory valuation
4. **Expiry Dates**: Set expiry dates for perishable products for timely alerts
5. **Notes**: Add notes to crops for context and future reference

## Troubleshooting

**Database Issues:**
- Delete `farm_management.db` to reset database
- Run `python app.py` again to recreate

**Port Already in Use:**
- Change port in app.py: `app.run(debug=True, port=5001)`
- Use different terminal for app

**Import Errors:**
- Ensure requirements.txt is installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.7+)

## Future Enhancements

- Weather integration for planting recommendations
- Mobile app version
- Multi-user farm collaboration
- Advanced reporting and analytics
- Export to PDF/CSV
- Soil analysis tracking
- Equipment maintenance logs
- Supply chain management
- Market price tracking

## Support

For issues or questions about the application, please review the code comments and templates.

## License

This Farm Management System is provided as-is for agricultural operations.

---

**Version**: 1.0
**Last Updated**: 2024
