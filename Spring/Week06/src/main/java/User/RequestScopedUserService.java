package User;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.context.annotation.ScopedProxyMode;
import org.springframework.stereotype.Service;
import org.springframework.web.context.WebApplicationContext;

@Service
@Scope(value = WebApplicationContext.SCOPE_REQUEST, proxyMode = ScopedProxyMode.TARGET_CLASS)
public class RequestScopedUserService extends UserService{
    @Autowired
    public RequestScopedUserService(UserRepository userRepository) {
        super(userRepository);
        System.out.println("RequestScopedUserService created");
    }
}
