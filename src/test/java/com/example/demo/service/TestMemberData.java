package com.example.demo.service;

import com.example.demo.domain.Member;
import com.example.demo.repository.MemberDao;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.aop.support.AopUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.assertTrue;


@SpringBootTest
public class TestMemberData {
    @Autowired
    private MemberService memberService;

    @Autowired
    private MemberServiceRequiredNew memberServiceRequiredNew;

    @Autowired
    private MemberDao memberRepository;

    @AfterEach
    public void afterEach(){
        memberRepository.clearDb();
    }

    @Test
    public void requiredTest() {
        // Given
        Member member1 = new Member("user1");
        Member member2 = new Member("error"); // 오류를 유발할 사용자

        try {
            // 트랜잭션이 시작된 상태에서 두 번의 join 호출
            memberService.join(member1); // 트랜잭션에 참여
            memberService.join(member2); // 예외 발생 → 전체 트랜잭션 롤백
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Then
        // 트랜잭션 롤백 여부 확인
        boolean isUser1Present = memberRepository.findByUsername("user1").isPresent();
        boolean isErrorPresent = memberRepository.findByUsername("error").isPresent();
        System.out.println("MemberService is proxied: " + AopUtils.isAopProxy(memberService));

        System.out.println("User1 present after rollback: " + isUser1Present);
        System.out.println("Error present after rollback: " + isErrorPresent);

        assertTrue(memberRepository.findByUsername("user1").isEmpty(), "User1 should be rolled back");
        assertTrue(memberRepository.findByUsername("error").isEmpty(), "Error should be rolled back");
    }

    @Test
    public void requiredNewTest() {
        // Given
        Member member1 = new Member();
        member1.setUsername("user2");

        Member member2 = new Member();
        member2.setUsername("error");

        try {
            memberServiceRequiredNew.joinNew(member1);
            memberServiceRequiredNew.joinNew(member2);

        } catch (Exception e) {
            e.printStackTrace();
        }

        // Then
        // member2는 롤백되었지만, member1은 커밋되어야 함
        assertTrue(memberRepository.findByUsername("user2").isPresent());
        assertTrue(memberRepository.findByUsername("error").isEmpty());
    }


}
