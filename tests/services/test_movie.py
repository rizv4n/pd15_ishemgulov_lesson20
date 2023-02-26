from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(
        id=1,
        title="Йеллоустоун",
        description="Владелец ранчо пытается сохранить землю своих предков.",
        trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
        year=2018,
        rating=8.6,
        genre_id=17,
        director_id=1
    )
    m2 = Movie(
        id=2,
        title="Рокетмен",
        description="История превращения застенчивого парня Реджинальда, талантливого музыканта из маленького...",
        trailer="https://youtu.be/VISiqVeKTq8",
        year=2019,
        rating=7.3,
        genre_id=18,
        director_id=4
    )

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2])
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "Чикаго",
            "description": "Рокси Харт мечтает о песнях и танцах и о том, как сравняться с самой Велмой Келли...",
            "trailer": "https://www.youtube.com/watch?v=YxzS_LzWdG8",
            "year": 2002,
            "rating": 7.2,
            "genre_id": 18,
            "director_id": 6
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "Дюна",
            "description": "Наследник знаменитого дома Атрейдесов Пол отправляется вместе с семьей на одну из самых...",
            "trailer": "https://www.youtube.com/watch?v=DOlTmIhEsg0",
            "year": 2021,
            "rating": 8.4,
            "genre_id": 7,
            "director_id": 11
        }

        self.movie_service.update(movie_d)
