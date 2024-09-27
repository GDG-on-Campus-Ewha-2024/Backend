package autoconfigure;
import hello.hello_spring.HelloSpringApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;


@Configuration
public class MyAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public HelloSpringApplication helloSpringApplication() {
        return new HelloSpringApplication();
    }
}
