package org.example;

import helllo.hello_spring.controller.HelloController;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AutoConfig {

    @Bean
    @ConditionalOnMissingBean
    public HelloController helloController() {
        return new HelloController();
    }
}
