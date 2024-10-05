package week3;


import java.util.HashMap;
import java.util.Map;

public class InMemoryUserRepository implements UserRepository {
    private final Map<Integer, User> userStorage = new HashMap<>();

    @Override
    public User findUserById(int id) {
        return userStorage.get(id);
    }

    @Override
    public void saveUser(User user) {
        if (userStorage.containsKey(user.getId())) {
            System.out.println("User with ID " + user.getId() + " already exists. Updating user.");
        }
        userStorage.put(user.getId(), user);
    }

}
