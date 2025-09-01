def test_imports():
    """Test da li se sve importuje bez greske"""
    from app.main import app
    from app.models.user import User
    from app.models.task import Task
    assert app is not None
    assert User is not None
    assert Task is not None
    print("All imports work!")

def tets_basic():
    """Osnovni test"""
    assert 1 + 1 ==2
    print("Basic test passed!")

