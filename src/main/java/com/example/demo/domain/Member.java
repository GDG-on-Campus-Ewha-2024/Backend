package com.example.demo.domain;

public class Member{
    private Long id;
    private String username;

    // Constructor
    public Member() {}

    public Member(String username) {
        this.username = username;
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}