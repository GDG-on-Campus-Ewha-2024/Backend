package com.example.demo.repository;

import com.example.demo.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository{
    List<Member> findAll();
    Optional<Member> findById(Long id);
    Optional<Member> findByUsername(String username);
    void deleteById(Long id);
    void save(Member member);
}

//public interface MemberRepository extends JpaRepository<Member, Long> { }
