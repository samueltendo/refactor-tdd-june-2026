class UserRepository {
  // Real version — would use a real database
  save(user) { throw new Error("Real DB call — don't use in tests"); }
  findById(id) { throw new Error("Real DB call — don't use in tests"); }
}

class FakeUserRepository {
  // FAKE — real logic, backed by memory instead of a database
  constructor() {
    this.users = new Map();
  }
  save(user) {
    this.users.set(user.id, user);
  }
  findById(id) {
    return this.users.get(id) ?? null;
  }
  findAll() {
    return [...this.users.values()];
  }
  delete(id) {
    this.users.delete(id);
  }
}

class UserService {
  constructor(repo) {
    this.repo = repo;
  }
  register(id, name) {
    this.repo.save({ id, name });
  }
  deactivate(id) {
    this.repo.delete(id);
  }
}

test('register then find', () => {
  const repo = new FakeUserRepository();
  const service = new UserService(repo);

  service.register('1', 'Sam');

  expect(repo.findById('1').name).toBe('Sam');
});

test('register then deactivate removes user', () => {
  const repo = new FakeUserRepository();
  const service = new UserService(repo);

  service.register('1', 'Sam');
  service.deactivate('1');

  expect(repo.findById('1')).toBeNull();
  expect(repo.findAll()).toEqual([]);
});


test('register returns user', () => {
  const repo = new FakeUserRepository();
  const service = new UserService(repo);

  service.register('1', 'Ashraf');

  expect(repo.findById('1')); // there's a user calle Ashraf
  expect(repo.findAll()).toEqual([]);
});
