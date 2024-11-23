package week5.service;

import org.springframework.stereotype.Service;
import week5.domain.User;
import week5.exception.UserNotFoundException;
import week5.repository.UserDao;
import week5.repository.UserRepository;

import java.util.List;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final UserDao userDao;

    public UserService(UserRepository userRepository, UserDao userDao) {
        this.userRepository = userRepository;
        this.userDao = userDao;
    }

    public List<User> findAll() {
        return userRepository.findAll();
    }

    public List<User> findUsersByUsername(String username) {
        return userDao.findByUsername(username); // Custom DAO 사용
    }

    public User saveUser(User user) {
        return userRepository.save(user);
    }

    public User findUserById(Long id) {
        return userRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException("User not found with id: " + id));
    }

    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new UserNotFoundException("User not found with id: " + id);
        }
        userRepository.deleteById(id);
    }

    public void clearDb() {
        userRepository.deleteAll();
    }

    public User findUserByEmail(String email) {
        return userDao.findByEmail(email);
    }

    public boolean isUsernameDuplicate(String username) {
        List<User> users = userDao.findByUsername(username);
        return !users.isEmpty();
    }
}
