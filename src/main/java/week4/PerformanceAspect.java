package week4;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class PerformanceAspect {

    @Around("@annotation(week4.MonitorPerformance)")
    public Object measurePerformance(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis(); // 시작 시간
        Object result;

        try {
            result = joinPoint.proceed(); // 메소드 실행
        } finally {
            long endTime = System.currentTimeMillis(); // 종료 시간
            String methodName = joinPoint.getSignature().toShortString();
            System.out.println(methodName + " 실행 시간: " + (endTime - startTime) + " ms");
        }

        return result;
    }
}