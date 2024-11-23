package User;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LifecycleUserService extends UserService {
    @Autowired
    public LifecycleUserService(UserRepository userRepository) {
        super(userRepository);
        System.out.println("LifecycleUserService created");
    }

    @PostConstruct
    public void init(){
        System.out.println("UserService initialized");
        System.out.println("LifecycleUserService initialized");
    }

    @PreDestroy
    public void destroy(){
        System.out.println("UserService destroyed");
        System.out.println("LifecycleUserService destroyed");
    }

}
