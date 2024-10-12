package User;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.context.annotation.ScopedProxyMode;
import org.springframework.stereotype.Service;
import org.springframework.web.context.WebApplicationContext;

@Service
@Scope(value = WebApplicationContext.SCOPE_SESSION, proxyMode = ScopedProxyMode.TARGET_CLASS)
public class SessionScopedUserService extends UserService {
    @Autowired
    public SessionScopedUserService(UserRepository userRepository) {
        super(userRepository);
        System.out.println("SessionScopedUserService created");
    }
}
