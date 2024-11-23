package com.example.demo.service;

import com.example.demo.domain.Member;
import com.example.demo.repository.MemberRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

@Service
public class MemberServiceRequiredNew {

    private final MemberRepository memberRepository;

    public MemberServiceRequiredNew(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void joinNew(Member member) {
        if ("error".equals(member.getUsername())) {
            throw new IllegalArgumentException("username == error");
        }
        memberRepository.save(member);
    }
}
