package User;

import org.springframework.boot.autoconfigure.data.jpa.JpaRepositoriesAutoConfiguration;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository{
    User findById(Long id);
    void save(User user);
}
