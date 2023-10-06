from etablissement import Etablissement
from user import User

p = Etablissement()

p.addUser(User('foo', 'bar'))
p.addUser(User('login', 'password'))

print(p.getUsers())

# p.deleteUser


print(p)


