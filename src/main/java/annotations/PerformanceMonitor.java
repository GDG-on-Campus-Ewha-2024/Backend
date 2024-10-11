package annotations;

//커스텀 어노테이션 정의
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.METHOD) // 메소드에 적용될 어노테이션
@Retention(RetentionPolicy.RUNTIME) // 런타임에 어노테이션 정보를 유지
public @interface PerformanceMonitor {
    // 필요에 따라 속성 추가 가능 (여기서는 없음)
}