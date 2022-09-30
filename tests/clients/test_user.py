import vcr

from doccano_client.client import DoccanoClient
from doccano_client.clients.user import UserClient
from doccano_client.models.user import User
from tests.conftest import cassettes_path


class TestUserClient:
    @classmethod
    def setup_class(cls):
        with vcr.use_cassette(str(cassettes_path / "user/login.yaml"), mode="once"):
            client = DoccanoClient("http://localhost:8000")
            client.login(username="admin", password="password")
        cls.client = UserClient(client)

    def test_get_profile(self):
        with vcr.use_cassette(str(cassettes_path / "user/get_profile.yaml"), mode="once"):
            user = self.client.get_profile()
            assert user.username == "admin"

    def test_list(self):
        with vcr.use_cassette(str(cassettes_path / "user/list.yaml"), mode="once"):
            users = self.client.list()
            assert all(isinstance(user, User) for user in users)
