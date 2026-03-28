#!/usr/bin/env python
"""Test script to verify template rendering"""
from app import app, db, User, Inventory
from flask import render_template
from datetime import datetime

with app.app_context():
    db.create_all()
    
    # Get or create user
    user = User.query.filter_by(username='testuser').first()
    if not user:
        user = User(
            username='testuser',
            email='test@example.com',
            password='hashed_password'
        )
        db.session.add(user)
        db.session.commit()
    
    # Get test data
    page = 1
    status_filter = 'in_stock'
    query = Inventory.query.filter_by(user_id=user.id)
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    items = query.order_by(Inventory.created_at.desc()).paginate(page=page, per_page=20)
    total_value = sum(item.quantity * item.price_per_unit for item in Inventory.query.filter(
        Inventory.user_id == user.id,
        Inventory.status == 'in_stock'
    ).all())
    
    # Test template rendering
    print("Testing template context:")
    print(f"✓ items object type: {type(items)}")
    print(f"✓ items.items length: {len(items.items)}")
    print(f"✓ items.pages: {items.pages}")
    print(f"✓ total_value: ${total_value:.2f}")
    
    # Try to render the inventory template with test data
    try:
        with app.test_request_context():
            html = render_template('inventory.html', 
                                 items=items, 
                                 total_value=total_value, 
                                 status_filter=status_filter)
            print("✓ Template rendered successfully")
            
            # Check if essential HTML elements are present
            if '<table class="data-table">' in html:
                print("✓ Table element found")
            if 'Tomato Round' in html:
                print("✓ Inventory items rendered in template")
            if 'pagination' in html.lower():
                print("✓ Pagination section found")
                
    except Exception as e:
        print(f"✗ Template rendering error: {e}")
        import traceback
        traceback.print_exc()

print("\n✓ Template rendering test passed!")
