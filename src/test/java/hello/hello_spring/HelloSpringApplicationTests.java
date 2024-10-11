package hello.hello_spring;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import hello.hello_spring.service.ExampleService;


@SpringBootTest(classes = HelloSpringApplication.class)
class HelloSpringApplicationTests {

	@Autowired
	private ExampleService exampleService; // ExampleService 주입

	@Test
	public void testRunHeavyProcess() {
		System.out.println("Starting heavy process test...");
		exampleService.runHeavyProcess(); // 성능 측정 대상 메소드 호출
	}
}
