package AOPexample;


import org.aspectj.lang.annotation.Aspect;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.stereotype.Component;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;


@EnableAspectJAutoProxy
@Aspect
@Component
public class PerformanceAspect {
    @Around("@annotation(PerformanceMonitor)")
    public Object monitorPerformance(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();

        Object result = joinPoint.proceed();

        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;

        System.out.println(joinPoint.getSignature() + " executed in " + executionTime + "ms");

        return result;
    }
}
