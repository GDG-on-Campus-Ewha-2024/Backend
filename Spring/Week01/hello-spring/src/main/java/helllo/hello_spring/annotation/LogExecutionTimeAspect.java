package helllo.hello_spring.annotation;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LogExecutionTimeAspect {

    @Around("@annotation(logExecutionTime)")
    public Object monitorExecution(ProceedingJoinPoint joinPoint, LogExecutionTime logExecutionTime) throws Throwable {
        long startTime = System.currentTimeMillis();

        Object result = joinPoint.proceed();

        long endTime = System.currentTimeMillis();

        if (logExecutionTime.logExecutionTime()) {
            System.out.println(joinPoint.getSignature() + " executed in " + (endTime - startTime) + " ms");
        }

        return result;
    }
}
