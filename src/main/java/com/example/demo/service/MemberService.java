package com.example.demo.service;

import org.springframework.stereotype.Service;
import com.example.demo.domain.Member;
import com.example.demo.repository.MemberRepository;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class MemberService {

    private final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    public List<Member> getAllMembers() {
        return memberRepository.findAll();
    }

    public Optional<Member> getMemberById(Long id) {
        return memberRepository.findById(id);
    }

    @Transactional(propagation = Propagation.REQUIRED, rollbackFor = Exception.class)
    public Member join(Member member) {
        if ("error".equals(member.getUsername())) {
            throw new IllegalArgumentException("username == error");
        }
        memberRepository.save(member);
        return member;
    }

    public Optional<Member> update(Long id, Member updatedMember) {
        Optional<Member> memberOptional = getMemberById(id);
        memberOptional.ifPresent(member -> member.setUsername(updatedMember.getUsername()));
        return memberOptional;
    }


    public void deleteById(Long id) {
        getMemberById(id); // id 존재 여부 확인하면서 예외 처리
        memberRepository.deleteById(id);
    }
}