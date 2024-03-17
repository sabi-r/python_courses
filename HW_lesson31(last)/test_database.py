import pytest
from database import create_dogs_table, insert_dog


@pytest.fixture
def database():
    connection = create_dogs_table()
    yield connection
    connection.close()


def test_check_breed(database):
    insert_dog(database, "Rex", "Labrador", 5, "Male")
    cursor = database.cursor()
    cursor.execute("SELECT breed FROM dogs WHERE name=?", ("Rex",))
    result = cursor.fetchone()
    assert result[0] == "Labrador"
