package aspect;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

//AOP를 활용한 성능 모니터링 클래스 구현
@Aspect
@Component
public class PerformanceAspect {

    private static final Logger logger = LoggerFactory.getLogger(PerformanceAspect.class);

    @Around("@annotation(annotations.PerformanceMonitor)")
    public Object monitorPerformance(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis(); // 메소드 실행 시작 시간

        Object result = joinPoint.proceed(); // 메소드 실행

        long endTime = System.currentTimeMillis(); // 메소드 실행 종료 시간
        long executionTime = endTime - startTime; // 실행 시간 계산
        System.out.println("[PERFORMANCE MONITOR] Method " + joinPoint.getSignature() + " executed in " + executionTime + " ms");
        logger.info("[PERFORMANCE MONITOR] Method " + joinPoint.getSignature() + " executed in " + executionTime + " ms");


        return result;
    }
}
