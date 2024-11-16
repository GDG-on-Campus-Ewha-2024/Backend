package week5.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import week5.domain.User;

public interface UserRepository extends JpaRepository<User, Long> {
}
