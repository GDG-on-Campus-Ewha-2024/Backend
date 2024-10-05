package User;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackageClasses = {UserRepository.class, UserSpringApplication.class})
public class UserSpringApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserSpringApplication.class, args);
    }
}
