import pytest, os, pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from app.data.db_schema import Base as Base_defined, User
from app.config import TestingConfig as config

@pytest.fixture
def db_init():
    engine = create_engine(config.DB_URL)
    Base_defined.metadata.drop_all(engine)
    Base_defined.metadata.create_all(engine)

    return Base_defined, engine

@pytest.fixture
def Base_reflection():
    engine = create_engine(config.DB_URL)
    Base_reflected = automap_base()
    Base_reflected.prepare(autoload_with=engine)

    return Base_reflected

def test_schema_creation():
    engine = create_engine(config.DB_URL)

    Base_defined.metadata.drop_all(engine)
    real_time_db_meta = MetaData()
    real_time_db_meta.reflect(bind = engine)
    assert len(real_time_db_meta.tables.keys()) == 0

    Base_defined.metadata.create_all(engine)
    real_time_db_meta = MetaData()
    real_time_db_meta.reflect(bind = engine)
    
    assert len(real_time_db_meta.tables.keys()) != 0

def test_data_insertion(db_init, Base_reflection):
    Base_defined, engine = db_init
    Base_reflected = Base_reflection

    # Add test admin user
    test_admin_user = User(username = 'demo')
    test_admin_user.set_password('password')
    assert test_admin_user.check_password('password')

    with Session(engine) as session:
        session.add(test_admin_user)
        session.commit()
        rows_count = session.query(User).count()
        assert rows_count != 0

    # Test data
    for file in ['BLOCK', 'DEPARTMENT', 'EVAL', 'LOCATION', 'QUESTION']:
        _df = pd.read_csv(os.path.join(config.RAW_TEST_DATA_DIR, file + '.csv'), on_bad_lines='skip')
        _df.to_sql(name = file, con = engine, if_exists = 'append', index = False)
        table_model = Base_reflected.classes[file]
        with Session(engine) as session:
            rows_count = session.query(table_model).count()
            assert rows_count != 0