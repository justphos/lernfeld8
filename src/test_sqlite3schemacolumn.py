from sqlite3schemacolumn import SQLite3SchemaColumn


def test_SQLite3SchemaColumn():
    # Test creating a new instance of SQLite3SchemaColumn
    column = SQLite3SchemaColumn(1, 'id', 'INTEGER', 1, None, 1)
    assert column.cid == 1
    assert column.name == 'id'
    assert column.type == 'INTEGER'
    assert column.notnull == 1
    assert column.dflt_value is None
    assert column.pk == 1

    # Test updating the values of an existing SQLite3SchemaColumn instance
    column.name = 'name'
    column.type = 'TEXT'
    column.notnull = 0
    column.dflt_value = 'NULL'
    column.pk = 0
    assert column.name == 'name'
    assert column.type == 'TEXT'
    assert column.notnull == 0
    assert column.dflt_value == 'NULL'
    assert column.pk == 0


def test_SQLite3SchemaColumn_equality():
    column1 = SQLite3SchemaColumn(1, 'id', 'INTEGER', 1, None, 1)
    column2 = SQLite3SchemaColumn(1, 'id', 'INTEGER', 1, None, 1)
    assert column1 == column2

    column3 = SQLite3SchemaColumn(2, 'name', 'TEXT', 0, 'NULL', 0)
    assert column1 != column3
