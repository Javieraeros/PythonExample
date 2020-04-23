from User import *
import time

begin_time = time.time()
# users = [User("Javi", "active"), User("Robot", "inactive"), User("Second robot", "active")]
#
# for user in users.copy():
#     print(user.name)
#     if user.status == "inactive":
#         users.remove(user)
#
# for user in users.copy():
#     print(user.name)

for i in range(0, 150000, 1):
    print("El valor es ", i)

finish_time = time.time()

print(finish_time - begin_time)
