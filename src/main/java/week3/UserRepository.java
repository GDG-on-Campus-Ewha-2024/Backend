package week3;

public interface UserRepository {
    User findUserById(int id);
    void saveUser(User user);
}
