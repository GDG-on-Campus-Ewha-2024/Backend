package hello.hello_spring.service;
import annotations.PerformanceMonitor;
import org.springframework.stereotype.Service;

@Service

public class ExampleService {

    @PerformanceMonitor
    public void runHeavyProcess() {
        // 성능 측정을 하고 싶은 알고리즘 또는 메소드
        try {
            Thread.sleep(2000); // 예시로 2초간 대기 (heavy process 시뮬레이션)
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Heavy process completed.");
    }
}
