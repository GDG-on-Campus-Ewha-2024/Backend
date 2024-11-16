package study.hello_spring.service;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import study.hello_spring.repository.MemberRepository;
import study.hello_spring.repository.MemoryMemberRepository;

@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
}
