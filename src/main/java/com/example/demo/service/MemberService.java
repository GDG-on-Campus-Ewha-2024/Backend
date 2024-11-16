package com.example.demo.service;

import org.springframework.stereotype.Service;
import com.example.demo.domain.Member;
import com.example.demo.exception.ResourceNotFoundException;
import com.example.demo.repository.MemberRepository;

import java.util.List;

@Service
public class MemberService {

    private final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    public List<Member> getAllMembers() {
        return memberRepository.findAll();
    }

    public Member getMemberById(Long id) {
        return memberRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Member not found with ID: " + id));
    }

    public Member getMemberByEmail(String email) {
        return memberRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Member not found with email: " + email));
    }

    public Member createMember(Member member) {
        return memberRepository.save(member);
    }

    public Member updateMember(Long id, Member updatedMember) {
        Member existingMember = getMemberById(id);
        existingMember.setUsername(updatedMember.getUsername());
        existingMember.setEmail(updatedMember.getEmail());
        return memberRepository.save(existingMember);
    }

    public void deleteMember(Long id) {
        if (!memberRepository.existsById(id)) {
            throw new ResourceNotFoundException("Member not found with ID: " + id);
        }
        memberRepository.deleteById(id);
    }
}