import sys 
import os 
import pytest 

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))


import db 
@pytest.fixture(autouse = True)
def use_temp_database(tmp_path, monkeypatch) :
    temp_db_path = tmp_path / "test_expenses.db"
    monkeypatch.setattr(db, "DB_PATH", str(temp_db_path))
    db.init_db()

def test_add_expense_success() :
    result = db.add_expense("2026-09-01", "Food", 250.0 , "Lunch")
    assert result is True 

    expenses = db.get_all_expenses() 
    assert len(expenses) == 1
    assert expenses[0][2] == "Food" 
    assert expenses[0][3] == 250.0 

def test_add_expense_invalid_date() :
    result = db.add_expense("2026-13-45", "Food", 100.0)
    assert result is False 

    expenses = db.get_all_expenses()
    assert len(expenses) == 0

def test_add_expense_negative_amount() :
    result = db.add_expense("2026-09-01", "Food", -50.0)
    assert result is False 

def test_add_expense_empty_category() :
    result = db.add_expense("2026-09-01", "", 100.0)
    assert result is False 

def test_delete_expense_success() :
    db.add_expense("2026-09-01", "Food", 250.0) 
    expenses = db.get_all_expenses() 
    expense_id = expenses[0][0]

    result = db.delete_expense(expense_id)
    assert result is True 


def test_delete_nonexistent_expense() :
    result = db.delete_expense(9999)
    assert result is False 


def test_update_expense_success() :
    db.add_expense("2026-09-01", "Food", 250.0) 
    expenses = db.get_all_expenses() 
    expense_id = expenses[0][0]

    result = db.update_expense(expense_id, amount = 500.0 )
    assert result is True 

    updated = db.get_all_expenses() 
    assert updated[0][3] == 500.0\


def test_update_nonexistent_expense() :
    result = db.update_expense(9999, amount = 500.0) 
    assert result is False 

def test_update_with_invalid_amount() :
    db.add_expense("2026-09-01", "Food", 250.0)
    expenses  = db.get_all_expenses() 
    expense_id = expenses[0][0] 

    result = db.update_expense(expense_id, amount = -100.0)
    assert result is False 
