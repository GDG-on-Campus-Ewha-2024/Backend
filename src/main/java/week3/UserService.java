package week3;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;

@Service
@Scope("singleton")
public class UserService {
    private final UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    // 비즈니스 로직 (간단한 사용자 추가 기능)
    public void addSingletonUser(int id, String name) {
        User user = new User(id, name); // 싱글톤 스코프에서 사용자 추가
        userRepository.saveUser(user);
        System.out.println("Singleton User added: " + user.getName());
    }

    public void addPrototypeUser(int id) {
        User user = new User(id, "Prototype User"); // 새로운 프로토타입 사용자 생성
        userRepository.saveUser(user);
        System.out.println("Prototype User added: " + user.getName());
    }

    @PostConstruct
    public void init() {
        System.out.println("Initializing UserService: Database connection established.");
    }

    @PreDestroy
    public void destroy() {
        System.out.println("Destroying UserService: Database connection closed.");
    }
}
