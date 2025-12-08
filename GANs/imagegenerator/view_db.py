#!/usr/bin/env python3
"""
Simple script to view database records
"""
from database import get_db, ImageRecord
from sqlalchemy import desc
import os

def view_records():
    """Display all image records from the database"""
    db = next(get_db())
    images = db.query(ImageRecord).order_by(desc(ImageRecord.created_at)).all()
    
    if not images:
        print('No records found in the database.')
        print('Generate some images first using the API!')
        return
    
    print(f'\n{"="*80}')
    print(f'Total records: {len(images)}')
    print(f'{"="*80}\n')
    
    for img in images:
        file_exists = "✓" if os.path.exists(img.image_path) else "✗"
        print(f'ID: {img.id}')
        print(f'Prompt: {img.prompt}')
        print(f'Image Path: {img.image_path} {file_exists}')
        print(f'Model: {img.model_name}')
        print(f'Created At: {img.created_at}')
        print('-' * 80)
        print()

if __name__ == "__main__":
    view_records()

