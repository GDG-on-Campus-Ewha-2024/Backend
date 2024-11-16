package com.example.demo.controller;

import org.springframework.hateoas.CollectionModel;
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

    // GET /api/members
    @GetMapping
    public CollectionModel<EntityModel<Member>> getAllMembers() {
        List<EntityModel<Member>> members = memberService.getAllMembers().stream()
                .map(member -> EntityModel.of(member,
                        WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class)
                                .getMemberById(member.getId())).withSelfRel(),
                        WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class)
                                .getAllMembers()).withRel("all-members")))
                .collect(Collectors.toList());
        return CollectionModel.of(members,
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getAllMembers()).withSelfRel());
    }

    // GET /api/members/{id}
    @GetMapping("/{id}")
    public EntityModel<Member> getMemberById(@PathVariable("id") Long id) {
        Member member = memberService.getMemberById(id);
        return EntityModel.of(member,
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getMemberById(id)).withSelfRel(),
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getAllMembers()).withRel("all-members"));
    }

    // POST /api/members
    @PostMapping
    public ResponseEntity<EntityModel<Member>> createMember(@RequestBody Member member) {
        Member createdMember = memberService.createMember(member);
        EntityModel<Member> model = EntityModel.of(createdMember,
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getMemberById(createdMember.getId())).withSelfRel(),
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getAllMembers()).withRel("all-members"));
        return ResponseEntity.created(WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class)
                .getMemberById(createdMember.getId())).toUri()).body(model);
    }

    // PUT /api/members/{id}
    @PutMapping("/{id}")
    public ResponseEntity<EntityModel<Member>> updateMember(@PathVariable("id") Long id, @RequestBody Member member) {
        Member updatedMember = memberService.updateMember(id, member);
        EntityModel<Member> model = EntityModel.of(updatedMember,
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getMemberById(id)).withSelfRel(),
                WebMvcLinkBuilder.linkTo(WebMvcLinkBuilder.methodOn(MemberController.class).getAllMembers()).withRel("all-members"));
        return ResponseEntity.ok(model);
    }

    // DELETE /api/members/{id}
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteMember(@PathVariable("id") Long id) {
        memberService.deleteMember(id);
        return ResponseEntity.noContent().build();
    }
}