package week5.service;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import week5.domain.User;
import week5.repository.UserDao;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
public class UserServiceTest {

    @Autowired
    private UserService userService;

    @BeforeEach
    void setup() {
        userService.saveUser(new User(null, "test1@example.com", "user1", "password1"));
        userService.saveUser(new User(null, "test2@example.com", "user2", "password2"));
    }

    @Test
    void testClearDb() {
        List<User> usersBeforeClear = userService.findAll();
        assertFalse(usersBeforeClear.isEmpty());

        userService.clearDb();

        List<User> usersAfterClear = userService.findAll();
        assertTrue(usersAfterClear.isEmpty());
    }
}
