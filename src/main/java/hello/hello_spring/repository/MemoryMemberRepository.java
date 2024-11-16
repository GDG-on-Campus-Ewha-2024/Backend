package hello.hello_spring.repository;

import hello.hello_spring.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.*;

@Repository
public class MemoryMemberRepository implements MemberRepository{

    //save를 위해 어딘가에 저장을 해야하니 map사용
    //키는 회원 id니까 long,값은 member
    //HashMap은 Map 인터페이스의 구현체(키-값의 쌍 형태)
    private static Map<Long,Member> store = new HashMap<>();
    //키값 생성해주는 sequence
    private static long sequence = 0L;
    @Override
    public Member save(Member member) {
        member.setId(++sequence); //넣기 전에 id 세팅
        store.put(member.getId(), member); //store에 저장(map에 저장됨)
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        //null일때를 대비하여 아래와 같이 코딩
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        //map을 돌면서, 매개변수로 들어온 name과 같은 애 있는지 보고,있으면 그걸 반환
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();

    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }
    public void clearStore(){
        store.clear();
    }
}
