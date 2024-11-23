package User;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/test")
public class TestController {
    @Autowired
    private RequestScopedUserService requestScopedUserService;

    @Autowired
    private SessionScopedUserService sessionScopedUserService;

    @Autowired
    private  LifecycleUserService lifecycleUserService;

    @GetMapping("/request-scope")
    public String testRequestScope(){
        requestScopedUserService.getUser(1L);
        return  "RequestScopedUserService called";
    }

    @GetMapping("/session-scope")
    public String testSessionScope(){
        sessionScopedUserService.getUser(1L);
        return  "SessionScopedUserService called";
    }

    @GetMapping("/lifecycle")
    public String testLifeCycle(){
        lifecycleUserService.getUser(1L);
        return  "LifecycleUserService called";
    }
}
