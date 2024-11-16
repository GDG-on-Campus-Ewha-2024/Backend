package hello.hello_spring.service;

import hello.hello_spring.domain.Member;
import hello.hello_spring.exception.MemberNotFoundException;
import hello.hello_spring.repository.MemberRepository;
import hello.hello_spring.repository.MemoryMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class memberService {
//    private final MemberRepository memberRepository = new MemoryMemberRepository();
    private final MemberRepository memberRepository;
    @Autowired
    public memberService(MemberRepository memberRepository){
        this.memberRepository = memberRepository;
    }

    //회원가입
    public Long join(Member member){
        //같은 이름 있는 중복회원x (옵셔널로 감싸사 반환 - ifPresent등의 메소드 사용가능)
        Optional<Member> result = memberRepository.findByName(member.getName());
        //result에 값이 있으면 동작
        result.ifPresent(m -> {
           throw new IllegalStateException("이미 존재하는 회원");
        });
        //
        memberRepository.save(member);
        return member.getId();
    }

    public List<Member> findMembers(){
        return memberRepository.findAll();
    }
    public Optional<Member> findOne(Long memberId) {
        Optional<Member> member = memberRepository.findById(memberId);
        if (member.isEmpty()) {
            throw new MemberNotFoundException(memberId + " not found");
        }
        return member;
    }
}

