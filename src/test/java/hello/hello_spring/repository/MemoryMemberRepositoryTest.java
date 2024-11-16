package hello.hello_spring.repository;

import hello.hello_spring.domain.Member;
import org.apache.el.parser.AstSetData;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class MemoryMemberRepositoryTest {

   MemoryMemberRepository repository = new MemoryMemberRepository();
    @AfterEach
    public void afterEach(){
    repository.clearStore();
    }

    @Test
    public void save(){
        Member member = new Member(); //멤버객체 만들어서
        member.setName("spring"); //네임지정

        repository.save(member); //리포지토리에 저장
        Member result = repository.findById(member.getId()).get(); //꺼내보기
        Assertions.assertEquals(member,result); //기대하는 것, 실제 데이터
        //최근 많이쓰는 assertions
        org.assertj.core.api.Assertions.assertThat(member).isEqualTo(result);

    }

    @Test
    public void findByname(){
        //객체 두개 만들어서 save(가입)
        Member member1 = new Member();
        member1.setName("sp1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("sp2");
        repository.save(member2);

        Member member = repository.findByName("sp1").get();
        org.assertj.core.api.Assertions.assertThat(member).isEqualTo(member1);
    }


}
