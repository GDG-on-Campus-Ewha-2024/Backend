package com.example.demo.controller;

import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.example.demo.domain.Member;
import com.example.demo.service.MemberService;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/members")
public class MemberController {

    private final MemberService memberService;

    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping
    public List<EntityModel<Member>> getAllMembers() {
        return memberService.getAllMembers().stream()
                .map(member -> EntityModel.of(member,
                        WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class)
                                .getMemberById(member.getId())).withSelfRel()))
                .collect(Collectors.toList());
    }

    @GetMapping("/{id}")
    public EntityModel<Member> getMemberById(@PathVariable("id") Long id) {
        Member member = memberService.getMemberById(id);
        return EntityModel.of(member,
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getAllMembers()).withRel("all-members"));
    }

    @PostMapping
    public ResponseEntity<Member> createMember(@RequestBody Member member) {
        Member createdMember = memberService.createMember(member);
        return ResponseEntity.created(
                        WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getMemberById(createdMember.getId())).toUri())
                .body(createdMember);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Member> updateMember(@PathVariable Long id, @RequestBody Member member) {
        Member updatedMember = memberService.updateMember(id, member);
        return ResponseEntity.ok(updatedMember);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteMember(@PathVariable Long id) {
        memberService.deleteMember(id);
        return ResponseEntity.noContent().build();
    }
}