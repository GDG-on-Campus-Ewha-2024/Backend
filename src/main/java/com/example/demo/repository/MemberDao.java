package com.example.demo.repository;

import com.example.demo.domain.Member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

class MemberRowMapper implements RowMapper<Member>{
    @Override
    public Member mapRow(ResultSet rs, int rowNum) throws SQLException{
        Member member = new Member();
        member.setId(rs.getLong("id"));
        member.setUsername(rs.getString("username"));

        return member;
    }
}

@Repository
public class MemberDao implements MemberRepository{
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Override
    public List<Member> findAll() {
        String sql = "SELECT * FROM member";
        return jdbcTemplate.query(sql, new MemberRowMapper());
    }

    @Override
    public Optional<Member> findById(Long id) {
        String sql = "SELECT * FROM member WHERE id = ?";
        try {
            return Optional.ofNullable(jdbcTemplate.queryForObject(sql, new MemberRowMapper(), id));
        } catch (EmptyResultDataAccessException e) {
            return Optional.empty();
        }
    }

    @Override
    public Optional<Member> findByUsername(String username) {
        String sql = "SELECT * FROM member WHERE username = ?";
        try {
            return Optional.ofNullable(
                    jdbcTemplate.queryForObject(sql, new MemberRowMapper(), username)
            );
        } catch (EmptyResultDataAccessException e) {
            return Optional.empty(); // null 대신 Optional.empty() 반환
        }
    }


    @Override
    public void deleteById(Long id) {
        String sql = "DELETE FROM member WHERE id = ?";
        jdbcTemplate.update(sql, id);
    }

    @Override
    public void save(Member member) {
        String sql = "INSERT INTO member (username) VALUES (?)";
        try {
            jdbcTemplate.update(sql, member.getUsername());
        } catch (Exception e) {
            throw new RuntimeException("Failed to save member: " + member.getUsername(), e);
        }
    }

    public void clearDb(){
        String sql = "DELETE FROM member";
        jdbcTemplate.update(sql);
    }

}
