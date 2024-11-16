package hello.hello_spring.controller;

import hello.hello_spring.domain.Member;
import hello.hello_spring.exception.MemberNotFoundException;
import hello.hello_spring.service.memberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.Link;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;

import java.util.List;
import java.util.Optional;

//@Controller
//public class MemberController {
//    private final memberService memberService;
//
//    @Autowired
//    public MemberController(hello.hello_spring.service.memberService memberService) {
//        this.memberService = memberService;
//    }
//
//    @GetMapping("/members/new")
//    public String createFrom(){
//        return "members/createMemberForm";
//    }
//
//    @PostMapping("/members/new")
//    public String create(MemberForm form){
//        Member member = new Member();
//        member.setName(form.getName());
//
//        memberService.join(member);
//
//        return "redirect:/"; //회원가입 끝나면 홈하면으로 리다이렉트
//    }
//
//    @GetMapping("/members")
//    public String list(Model model){
//        //멤버리스트를 모델에 담아서 화면에 넘긴다
//        List<Member> members = memberService.findMembers();
//        model.addAttribute("members",members);
//        return "members/memberList";
//
//    }
//}


@RestController
public class MemberController {

    private final memberService memberService;
    @Autowired
    public MemberController(memberService memberService) {
        this.memberService = memberService;
    }

//    @GetMapping("/Member/{id}")
//    public Member getMember(@PathVariable("id") Long id) {
//        return memberService.findOne(id)
//                .orElseThrow(() -> new MemberNotFoundException(id + " not found"));
//    }

    @GetMapping("/Member/all")
    public List<Member> getAllMember() {
        return memberService.findMembers();
    }

    @PostMapping("/Member/new/{name}")
    public void putMember(@PathVariable("name") String name) {
        Member member = new Member();
        member.setName(name);

        memberService.join(member);
    }

    //특정 회원 반환 - hateoas 사용버전
    @GetMapping("/Member/{id}")
    public EntityModel<Member> getMember(@PathVariable("id") Long id) {

        Member member = memberService.findOne(id)
                .orElseThrow(() -> new MemberNotFoundException(id + " not found"));

        // 리턴 객체에 링크 추가
        EntityModel<Member> memberModel = EntityModel.of(member);
        Link selfLink = WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getMember(id)).withSelfRel();


        // 링크 추가
        memberModel.add(selfLink);


        return memberModel;
    }

}
