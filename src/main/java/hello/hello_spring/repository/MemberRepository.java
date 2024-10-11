package hello.hello_spring.repository;

import hello.hello_spring.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    //회원이 저장되고, 저장된 회원이 반환됨
    Member save(Member member);

    //id,name으로 회원을 찾음
    //null 처리 시 옵셔널로 감싸서 처리하는 방식을 최근 선호
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);

    //저장된 모든 회원 반환
    List<Member> findAll();
}
