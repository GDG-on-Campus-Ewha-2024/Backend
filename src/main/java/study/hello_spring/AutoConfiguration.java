package study.hello_spring;

import study.hello_spring.controller.HelloController;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.boot.autoconfigure.condition.ConditionalOnClass;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;

@Configuration
@ConditionalOnClass(HelloController.class)
public class AutoConfiguration {

    @Bean
    @ConditionalOnMissingBean(HelloController.class)
    public HelloController helloController() {
        return new HelloController();
    }
}
