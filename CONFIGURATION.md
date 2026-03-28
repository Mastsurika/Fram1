# Configuration & Setup Guide

## Application Configuration

### Changing the Port

By default, the application runs on port 5000. To change this:

1. Open `app.py` in a text editor
2. Find the last line: `app.run(debug=True, port=5000)`
3. Change `5000` to your desired port number (e.g., `8080`, `3000`)
4. Save the file
5. Restart the application

### Disabling Debug Mode

For production use, disable debug mode:

1. Open `app.py`
2. Find: `app.run(debug=True, port=5000)`
3. Change to: `app.run(debug=False, port=5000)`
4. Save and restart

### Changing the Secret Key

For production use, change the secret key:

1. Open `app.py`
2. Find: `app.config['SECRET_KEY'] = 'your-secret-key-change-this'`
3. Replace with a random string (recommended: 32+ characters)
   - For example: `app.config['SECRET_KEY'] = 'farm_app_2024_secure_key_xyz123abc'`
4. Save and restart

## Database Configuration

### Database Location

The SQLite database is stored at: `farm_management.db` in the project root.

### Reset Database

To start fresh with a clean database:

1. Close the application
2. Delete `farm_management.db` file
3. Start the application again
4. A new database will be created automatically

### Database Backup

To backup your data:

1. Stop the application
2. Copy `farm_management.db` to a safe location
3. Rename the copy with date (e.g., `farm_management_backup_2024-01-15.db`)

### Database Restore

To restore from a backup:

1. Stop the application
2. Replace `farm_management.db` with your backup (rename it back)
3. Start the application

## Virtual Environment Management

### Why Virtual Environment?

A virtual environment keeps project dependencies isolated, preventing conflicts with other Python projects.

### Create New Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Deactivate Virtual Environment

```bash
deactivate
```

### Delete Virtual Environment

```bash
rmdir /s venv    (Windows)
rm -rf venv      (Mac/Linux)
```

## Dependency Management

### View Installed Packages

```bash
pip list
```

### Update All Packages

```bash
pip install --upgrade -r requirements.txt
```

### Add New Package

```bash
pip install package-name
pip freeze > requirements.txt
```

### Install from requirements.txt

```bash
pip install -r requirements.txt
```

## Troubleshooting Common Issues

### Issue: "Python not found"
**Solution:**
- Install Python 3.7+ from python.org
- Make sure to check "Add Python to PATH" during installation

### Issue: "No module named flask"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
**Solution:**
- Find what's using port 5000: `netstat -ano | findstr :5000` (Windows)
- Change port in app.py to something else (e.g., 5001, 8000)

### Issue: "Permission denied"
**Solution:**
- Run command prompt/terminal as Administrator
- Or change file permissions

### Issue: "Connection refused when accessing localhost:5000"
**Solution:**
- Check if application is running
- Check if you're using the correct port
- Try http://127.0.0.1:5000 instead
- Disable firewall temporarily

## Performance Tuning

### For Small Farms (< 100 crops)
- Default configuration is fine

### For Large Farms (> 1000 crops)
Consider:
- Using PostgreSQL instead of SQLite
- Adding database indexes
- Implementing caching

### Enable Caching (Django/Flask optimization)
Contact support for advanced optimization.

## Security Best Practices

### Local Use Only
✓ Current setup is suitable for personal farm management

### If Hosting Remotely
✗ Do NOT use default configuration
- Change SECRET_KEY (required)
- Set debug=False (required)
- Use HTTPS/SSL
- Add password requirements
- Implement user role management
- Use environment variables for secrets

### Password Security
- Minimum 8 characters recommended
- Use mix of uppercase, lowercase, numbers
- Avoid common words

### Data Protection
- Regularly backup farm_management.db
- Don't share login credentials
- Keep software updated

## System Requirements for Production

### Recommended Specs
- CPU: 2+ cores
- RAM: 2GB minimum
- Storage: 10GB (for growth)
- Network: Stable connection

### Supported Operating Systems
- Windows 7, 8, 10, 11
- macOS 10.12+
- Linux (Ubuntu 18.04+, Debian 10+)

## Advanced Configuration

### Custom Database

To use a different database (PostgreSQL, MySQL) instead of SQLite:

1. Install database driver: `pip install psycopg2` (PostgreSQL)
2. Modify `app.config['SQLALCHEMY_DATABASE_URI']` in app.py
3. Example for PostgreSQL:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/farmdb'
   ```

### Email Notifications

To add email alerts (requires additional setup):

1. Install Flask-Mail: `pip install Flask-Mail`
2. Configure SMTP settings in app.py
3. Modify alert templates

### SSL/HTTPS Setup

For production (requires certificate):

1. Obtain SSL certificate
2. Install Gunicorn: `pip install gunicorn`
3. Run with SSL: `gunicorn --certfile=cert.pem --keyfile=key.pem app:app`

## Deployment Options

### Option 1: Local Network
- Run on home server/computer
- Access from local network
- No internet required

### Option 2: Cloud Hosting
- Heroku
- PythonAnywhere
- DigitalOcean
- AWS

### Option 3: Dedicated Server
- VPS (Virtual Private Server)
- Dedicated hosting
- Self-managed

## Monitoring & Maintenance

### Check Application Logs
Monitor console output for errors

### Regular Updates
- Check for Python updates
- Update packages monthly: `pip install --upgrade -r requirements.txt`

### Database Maintenance
- Periodic backups
- Archive old data periodically
- Monitor database size

## Performance Monitoring

### Enable Slow Query Logging
Add to app.py before app.run():
```python
if not app.debug:
    app.logger.setLevel(logging.INFO)
```

---

For more help, refer to the README.md or QUICK_START.md
