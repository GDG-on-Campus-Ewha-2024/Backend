package autoconfigure;

import hello.hello_spring.HelloSpringApplication;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public HelloSpringApplication helloSpringApplication(){
        return new HelloSpringApplication();
    }
}
