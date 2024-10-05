package helllo.hello_spring.service;

import helllo.hello_spring.domain.User;
import helllo.hello_spring.repository.UserRepository;
import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import java.util.NoSuchElementException;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Scope("session")
public class UserService {

    private final UserRepository userRepository;

    public String getUserName(Long userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new NoSuchElementException("User not found with id: " + userId));
        return user.getName();
    }

    @PostConstruct
    public void init() {
        System.out.println("UserService 초기화 - DB 연결");
    }

    @PreDestroy
    public void destroy() {
        System.out.println("UserService 소멸 - DB 연결 해제");
    }
}
