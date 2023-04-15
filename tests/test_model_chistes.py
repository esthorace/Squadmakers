from pytest import fixture
from sqlmodel import Session, create_engine

from app.models.model_chistes import Chiste


@fixture(scope="module")
def db():
    engine = create_engine("sqlite:///:memory:")
    with engine.begin() as connection:
        Chiste.metadata.create_all(connection)
    yield engine
    Chiste.metadata.drop_all(engine)


def test_chiste_base(db):
    chiste_data = {
        "chiste": "¿Por qué los programadores prefieren el frío?", "pokemon": "Charmander"}
    chiste = Chiste(**chiste_data)

    with Session(db) as session:
        session.add(chiste)
        session.commit()

    with Session(db) as session:
        result = session.query(Chiste).filter_by(
            chiste=chiste_data["chiste"]).first()
    assert result is not None
    assert result.chiste == chiste_data["chiste"]
    assert result.pokemon == chiste_data["pokemon"]
