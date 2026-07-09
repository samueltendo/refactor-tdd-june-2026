class UserRepository:
    """Real version — would use a real database."""
    def save(self, user):
        raise NotImplementedError("Real DB call — don't use in tests")

    def find_by_id(self, user_id):
        raise NotImplementedError("Real DB call — don't use in tests")


class FakeUserRepository:
    """FAKE — real logic, backed by memory instead of a database."""
    def __init__(self):
        self._users = {}

    def save(self, user):
        self._users[user['id']] = user

    def find_by_id(self, user_id):
        return self._users.get(user_id)

    def find_all(self):
        return list(self._users.values())

    def delete(self, user_id):
        self._users.pop(user_id, None)


class UserService:
    def __init__(self, repo):
        self.repo = repo

    def register(self, user_id, name):
        self.repo.save({'id': user_id, 'name': name})

    def deactivate(self, user_id):
        self.repo.delete(user_id)


def test_register_then_find():
    repo = UserRepository()
    service = UserService(repo)

    service.register('1', 'Sam')

    assert repo.find_by_id('1')['name'] == 'Sam'


def test_register_then_deactivate_removes_user():
    repo = FakeUserRepository()
    service = UserService(repo)

    service.register('1', 'Sam')
    service.deactivate('1')

    assert repo.find_by_id('1') is None
    assert repo.find_all() == []
