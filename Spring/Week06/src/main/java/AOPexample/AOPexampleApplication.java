package AOPexample;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@SpringBootApplication
@EnableAspectJAutoProxy
public class AOPexampleApplication {
    public static void main(String[] args) {
        SpringApplication.run(AOPexampleApplication.class, args);
    }
}
