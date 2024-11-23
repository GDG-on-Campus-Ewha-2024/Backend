package AOPexample;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AOPexampleController {

    @Autowired
    private SampleService sampleService;

    @GetMapping("/aopexample")
    public String monitorPerformance(){
        sampleService.performTask();
        return "Performance task executed. Check the console for details.";
    }
}
