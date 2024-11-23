package com.example.demo.controller;

import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.example.demo.domain.Member;
import com.example.demo.service.MemberService;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/members")
public class MemberController {

    private final MemberService memberService;

    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    // POST /api/members
    @PostMapping
    public ResponseEntity<Member> createMember(@RequestBody Member member) {
        Member createdMember = memberService.join(member);
        return ResponseEntity.status(HttpStatus.CREATED).body(createdMember);
    }

    // GET /api/members
    @GetMapping
    public ResponseEntity<List<Member>> getAllMembers(){
        return ResponseEntity.ok(memberService.getAllMembers());
    }

//    // GET /api/members/{id}
//    @GetMapping("/{id}")
//    public ResponseEntity<Member> getMemberById(@PathVariable("id") Long id) {
//        return ResponseEntity.ok(memberService.getMemberById(id));
//    }

    // GET /api/members/{id}
    @GetMapping("/{id}")
    public ResponseEntity<EntityModel<Optional<Member>>> getMemberById(@PathVariable("id") Long id) {
        Optional<Member> member = memberService.getMemberById(id);

        // HATEOAS 링크 추가
        EntityModel<Optional<Member>> memberModel = EntityModel.of(member,
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getMemberById(id)).withSelfRel(),
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getAllMembers()).withRel("all-members")
        );

        return ResponseEntity.ok(memberModel);
    }

    // PUT /api/members/{id}
    @PutMapping("/{id}")
    public ResponseEntity<Optional<Member>> updateMember(@PathVariable("id") Long id, @RequestBody Member member) {
        return ResponseEntity.ok(memberService.update(id, member));
    }

    // DELETE /api/members/{id}
    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteMember(@PathVariable("id")Long id) {
        memberService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}