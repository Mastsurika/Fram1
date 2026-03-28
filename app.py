from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
from functools import wraps
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///farm_management.db')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CropField(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    field_name = db.Column(db.String(120), nullable=False)
    field_area = db.Column(db.Float, nullable=False)  # in square meters
    location = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CropRound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field_id = db.Column(db.Integer, db.ForeignKey('crop_field.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    crop_name = db.Column(db.String(120), nullable=False)
    planting_date = db.Column(db.DateTime, nullable=False)
    estimated_harvest_date = db.Column(db.DateTime, nullable=False)
    actual_harvest_date = db.Column(db.DateTime, nullable=True)
    quantity_planted = db.Column(db.Float, nullable=False)  # in kg
    quantity_harvested = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(20), default='planting')  # planting, growing, ready, harvested
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_round_id = db.Column(db.Integer, db.ForeignKey('crop_round.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)  # watering, fertilizing, weeding, spraying, etc
    activity_date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)
    quantity_used = db.Column(db.Float, nullable=True)  # for chemicals, water, etc
    unit = db.Column(db.String(20), nullable=True)  # liters, kg, etc
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)  # kg, bags, liters, etc
    price_per_unit = db.Column(db.Float, nullable=False)
    harvest_date = db.Column(db.DateTime, nullable=True)
    expiry_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default='in_stock')  # in_stock, sold, expired
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class FinancialRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    record_type = db.Column(db.String(20), nullable=False)  # income, expense
    category = db.Column(db.String(50), nullable=False)  # seed, labor, sales, other
    description = db.Column(db.Text, nullable=True)
    quantity = db.Column(db.Float, nullable=True)
    unit = db.Column(db.String(20), nullable=True)
    unit_price = db.Column(db.Float, nullable=True)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    record_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def update_expired_inventory(user_id):
    """Update inventory items that have expired"""
    now = datetime.now()
    expired_items = Inventory.query.filter(
        Inventory.user_id == user_id,
        Inventory.status == 'in_stock',
        Inventory.expiry_date != None,
        Inventory.expiry_date < now
    ).all()
    
    for item in expired_items:
        item.status = 'expired'
    
    if expired_items:
        db.session.commit()
        app.logger.info(f"Updated {len(expired_items)} items to expired status for user {user_id}")

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            return render_template('register.html', error='รหัสผ่านไม่ตรงกัน')
        
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='ชื่อผู้ใช้นี้มีอยู่แล้ว')
        
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    
    # Get statistics
    fields = CropField.query.filter_by(user_id=user_id).count()
    active_crops = CropRound.query.filter(
        CropRound.user_id == user_id,
        CropRound.status.in_(['planting', 'growing'])
    ).count()
    
    inventory_items = Inventory.query.filter(
        Inventory.user_id == user_id,
        Inventory.status == 'in_stock'
    ).all()
    
    total_inventory_value = sum(item.quantity * item.price_per_unit for item in inventory_items)
    
    # Get financial summary
    financial_records = FinancialRecord.query.filter_by(user_id=user_id).all()
    total_income = sum(r.amount for r in financial_records if r.record_type == 'income')
    total_expense = sum(r.amount for r in financial_records if r.record_type == 'expense')
    
    # Get alerts (crops ready for harvest)
    alerts = CropRound.query.filter(
        CropRound.user_id == user_id,
        CropRound.status == 'ready'
    ).all()
    
    # Get recent activities
    recent_activities = Activity.query.filter_by(user_id=user_id).order_by(
        Activity.created_at.desc()
    ).limit(5).all()
    
    return render_template('dashboard.html',
                         fields=fields,
                         active_crops=active_crops,
                         alerts=alerts,
                         inventory_count=len(inventory_items),
                         total_income=total_income,
                         total_expense=total_expense,
                         recent_activities=recent_activities)

@app.route('/crop-management')
@login_required
def crop_management():
    user_id = session['user_id']
    fields = CropField.query.filter_by(user_id=user_id).all()
    # Get all active crop rounds for display
    active_crops = CropRound.query.filter(
        CropRound.user_id == user_id,
        CropRound.status != 'harvested'
    ).all()
    return render_template('crop_management.html', fields=fields, active_crops=active_crops)

@app.route('/field/add', methods=['GET', 'POST'])
@login_required
def add_field():
    if request.method == 'POST':
        try:
            user_id = session['user_id']
            field = CropField(
                user_id=user_id,
                field_name=request.form.get('field_name'),
                field_area=float(request.form.get('field_area', 0)),
                location=request.form.get('location')
            )
            db.session.add(field)
            db.session.commit()
            return redirect(url_for('crop_management'))
        except ValueError:
            db.session.rollback()
            return render_template('add_field.html', error='ขนาดพื้นที่ไม่ถูกต้อง กรุณากรอกเป็นตัวเลข')
    
    return render_template('add_field.html')

@app.route('/field/<int:field_id>/crop/add', methods=['GET', 'POST'])
@login_required
def add_crop_round(field_id):
    user_id = session['user_id']
    field = CropField.query.get_or_404(field_id)
    
    if field.user_id != user_id:
        return redirect(url_for('crop_management'))
    
    if request.method == 'POST':
        try:
            crop = CropRound(
                field_id=field_id,
                user_id=user_id,
                crop_name=request.form.get('crop_name'),
                planting_date=datetime.strptime(request.form.get('planting_date'), '%Y-%m-%d'),
                estimated_harvest_date=datetime.strptime(request.form.get('estimated_harvest_date'), '%Y-%m-%d'),
                quantity_planted=float(request.form.get('quantity_planted', 0)),
                notes=request.form.get('notes')
            )
            db.session.add(crop)
            db.session.commit()
            return redirect(url_for('crop_management'))
        except (ValueError, TypeError):
            db.session.rollback()
            return render_template('add_crop_round.html', field=field, error='ข้อมูลไม่ถูกต้อง กรุณาตรวจสอบอีกครั้ง')
    
    return render_template('add_crop_round.html', field=field)

@app.route('/crop/<int:crop_id>')
@login_required
def view_crop(crop_id):
    user_id = session['user_id']
    crop = CropRound.query.get_or_404(crop_id)
    
    if crop.user_id != user_id:
        return redirect(url_for('crop_management'))
    
    field = CropField.query.get(crop.field_id)
    activities = Activity.query.filter_by(crop_round_id=crop_id).order_by(
        Activity.activity_date.desc()
    ).all()
    
    days_until_harvest = (crop.estimated_harvest_date - datetime.now()).days if crop.status != 'harvested' else 0
    
    return render_template('view_crop.html', crop=crop, field=field, activities=activities, days_until_harvest=days_until_harvest)

@app.route('/crop/<int:crop_id>/activity/add', methods=['POST'])
@login_required
def add_activity(crop_id):
    user_id = session['user_id']
    crop = CropRound.query.get_or_404(crop_id)
    
    if crop.user_id != user_id:
        return redirect(url_for('crop_management'))
    
    quantity_str = request.form.get('quantity_used')
    quantity_used = None
    if quantity_str and quantity_str.strip():
        try:
            quantity_used = float(quantity_str)
        except ValueError:
            quantity_used = None

    activity_date = datetime.now()
    activity_date_str = request.form.get('activity_date')
    if activity_date_str and activity_date_str.strip():
        try:
            activity_date = datetime.fromisoformat(activity_date_str)
        except ValueError:
            try:
                activity_date = datetime.strptime(activity_date_str, '%Y-%m-%d %H:%M')
            except ValueError:
                activity_date = datetime.now()

    activity = Activity(
        crop_round_id=crop_id,
        user_id=user_id,
        activity_type=request.form.get('activity_type'),
        description=request.form.get('description'),
        activity_date=activity_date,
        quantity_used=quantity_used,
        unit=request.form.get('unit') or None
    )
    db.session.add(activity)
    db.session.commit()
    
    return redirect(url_for('view_crop', crop_id=crop_id))

@app.route('/crop/<int:crop_id>/harvest', methods=['POST'])
@login_required
def harvest_crop(crop_id):
    user_id = session['user_id']
    crop = CropRound.query.get_or_404(crop_id)
    
    if crop.user_id != user_id:
        return redirect(url_for('crop_management'))
    
    try:
        quantity_harvested = float(request.form.get('quantity_harvested', 0))
        price_per_unit = float(request.form.get('price_per_unit', 0))
        
        crop.actual_harvest_date = datetime.now()
        crop.quantity_harvested = quantity_harvested
        crop.status = 'harvested'
        
        # Add to inventory with 10-day expiry
        inventory = Inventory(
            user_id=user_id,
            product_name=crop.crop_name,
            quantity=quantity_harvested,
            unit='kg',
            price_per_unit=price_per_unit,
            harvest_date=crop.actual_harvest_date,
            expiry_date=crop.actual_harvest_date + timedelta(days=10)
        )
        db.session.add(inventory)
        db.session.commit()
    except ValueError:
        db.session.rollback()
        return redirect(url_for('view_crop', crop_id=crop_id))
    
    return redirect(url_for('view_crop', crop_id=crop_id))

@app.route('/alerts')
@login_required
def alerts():
    user_id = session['user_id']
    
    # Update expired inventory items
    update_expired_inventory(user_id)
    
    now = datetime.now()
    
    # Get crops ready for harvest (estimated harvest date is within 7 days or passed)
    ready_crops = CropRound.query.filter(
        CropRound.user_id == user_id,
        CropRound.status.in_(['planting', 'growing']),
        CropRound.estimated_harvest_date <= now + timedelta(days=7)
    ).order_by(CropRound.estimated_harvest_date).all()
    
    # Get inventory alerts (items expiring soon)
    inventory_alerts = Inventory.query.filter(
        Inventory.user_id == user_id,
        Inventory.status == 'in_stock',
        Inventory.expiry_date != None,
        Inventory.expiry_date <= now + timedelta(days=7)
    ).order_by(Inventory.expiry_date).all()
    
    return render_template('alerts.html', ready_crops=ready_crops, inventory_alerts=inventory_alerts, now=now)

@app.route('/activity-log')
@login_required
def activity_log():
    user_id = session['user_id']
    page = request.args.get('page', 1, type=int)
    activities = Activity.query.filter_by(user_id=user_id).order_by(
        Activity.activity_date.desc()
    ).paginate(page=page, per_page=20)
    
    return render_template('activity_log.html', activities=activities)

@app.route('/inventory')
@login_required
def inventory():
    user_id = session['user_id']
    
    # Update expired inventory items
    update_expired_inventory(user_id)
    
    page = request.args.get('page', 1, type=int)
    
    status_filter = request.args.get('status', 'all')
    query = Inventory.query.filter_by(user_id=user_id)
    
    # ในหน้าสินค้าทั้งหมด (all) ให้แสดงเฉพาะ in_stock เท่านั้น
    if status_filter == 'all':
        query = query.filter_by(status='in_stock')
    elif status_filter in ['in_stock', 'sold', 'expired']:
        query = query.filter_by(status=status_filter)
    else:
        status_filter = 'all'
        query = query.filter_by(status='in_stock')
    
    try:
        items = query.order_by(Inventory.created_at.desc()).paginate(page=page, per_page=20)
    except Exception as e:
        app.logger.error(f"Error paginating inventory: {e}")
        items = None
    
    try:
        total_value = sum(item.quantity * item.price_per_unit for item in Inventory.query.filter(
            Inventory.user_id == user_id,
            Inventory.status == 'in_stock'
        ).all())
    except Exception as e:
        app.logger.error(f"Error calculating inventory value: {e}")
        total_value = 0
    
    return render_template('inventory.html', items=items, total_value=total_value, status_filter=status_filter)

@app.route('/financial-records', methods=['GET', 'POST'])
@login_required
def financial_records():
    user_id = session['user_id']
    if request.method == 'POST':
        record_type = request.form.get('record_type')
        category = request.form.get('category')
        description = request.form.get('description')
        quantity = None
        unit_price = None
        amount = 0.0

        try:
            if request.form.get('quantity'):
                quantity = float(request.form.get('quantity'))
        except ValueError:
            quantity = None

        unit = request.form.get('unit') or None

        try:
            if request.form.get('unit_price'):
                unit_price = float(request.form.get('unit_price'))
        except ValueError:
            unit_price = None

        try:
            if request.form.get('amount'):
                amount = float(request.form.get('amount'))
        except ValueError:
            amount = 0.0

        record_date = datetime.utcnow()
        date_input = request.form.get('record_date')
        if date_input:
            try:
                record_date = datetime.fromisoformat(date_input)
            except ValueError:
                try:
                    record_date = datetime.strptime(date_input, '%Y-%m-%d %H:%M')
                except ValueError:
                    record_date = datetime.utcnow()

        if amount <= 0 and quantity is not None and unit_price is not None:
            amount = quantity * unit_price

        fr = FinancialRecord(
            user_id=user_id,
            record_type=record_type,
            category=category,
            description=description,
            quantity=quantity,
            unit=unit,
            unit_price=unit_price,
            amount=amount,
            record_date=record_date
        )
        db.session.add(fr)
        db.session.commit()
        return redirect(url_for('financial_records'))

    records = FinancialRecord.query.filter_by(user_id=user_id).order_by(FinancialRecord.record_date.desc()).all()
    total_income = sum(r.amount for r in records if r.record_type == 'income')
    total_expense = sum(r.amount for r in records if r.record_type == 'expense')
    net_balance = total_income - total_expense
    seed_cost = sum(r.amount for r in records if r.record_type == 'expense' and r.category.lower() in ['seed', 'เมล็ดพันธุ์', 'เมล็ด'])
    labor_cost = sum(r.amount for r in records if r.record_type == 'expense' and r.category.lower() in ['labor', 'แรงงาน', 'คนงาน'])
    labor_count = sum(r.quantity for r in records if r.record_type == 'expense' and r.category.lower() in ['labor', 'แรงงาน', 'คนงาน'] and r.quantity)
    sales_revenue = sum(r.amount for r in records if r.record_type == 'income' and r.category.lower() in ['sales', 'ขายสินค้า', 'ขาย'])

    return render_template(
        'financial_record.html',
        records=records,
        total_income=total_income,
        total_expense=total_expense,
        net_balance=net_balance,
        seed_cost=seed_cost,
        labor_cost=labor_cost,
        labor_count=labor_count,
        sales_revenue=sales_revenue
    )

@app.route('/inventory/<int:item_id>/update-quantity', methods=['POST'])
@login_required
def update_inventory_quantity(item_id):
    user_id = session['user_id']
    item = Inventory.query.get_or_404(item_id)
    
    if item.user_id != user_id:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        data = request.get_json()
        new_status = data.get('status', item.status)
        
        # ถ้าสถานะเปลี่ยนเป็น 'sold' และก่อนหน้านี้ไม่ใช่ 'sold' ให้บันทึกการขาย
        if new_status == 'sold' and item.status != 'sold':
            fr = FinancialRecord(
                user_id=user_id,
                record_type='income',
                category='sales',
                description=f"ขาย {item.product_name} จำนวน {item.quantity} {item.unit}",
                quantity=item.quantity,
                unit=item.unit,
                unit_price=item.price_per_unit,
                amount=item.quantity * item.price_per_unit,
                record_date=datetime.utcnow()
            )
            db.session.add(fr)
        
        item.quantity = float(data.get('quantity', 0))
        item.status = new_status
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/reports')
@login_required
def reports():
    user_id = session['user_id']
    
    # Get all crop rounds
    all_crops = CropRound.query.filter_by(user_id=user_id).all()
    
    # Calculate statistics
    total_harvested = sum(crop.quantity_harvested for crop in all_crops if crop.quantity_harvested)
    total_crops = len([c for c in all_crops if c.status == 'harvested'])
    
    # Get inventory summary
    inventory_items = Inventory.query.filter(
        Inventory.user_id == user_id,
        Inventory.status == 'in_stock'
    ).all()
    
    total_inventory_value = sum(item.quantity * item.price_per_unit for item in inventory_items)
    
    return render_template('reports.html',
                         total_crops=total_crops,
                         total_harvested=total_harvested,
                         all_crops=all_crops,
                         inventory_value=total_inventory_value,
                         inventory_items=inventory_items)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
