package AOPexample;

import org.springframework.stereotype.Service;

@Service
public class SampleService {
    @PerformanceMonitor
    public void performTask() {
        int sum = 0;
        for (int i = 0; i < 1000; i++) {
            sum += i;
        }
        System.out.println("Sum = " + sum);
    }
}
