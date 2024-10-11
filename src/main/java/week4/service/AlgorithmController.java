package week4.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AlgorithmController {

    @Autowired
    private AlgorithmService algorithmService;

    @GetMapping("/run-algorithm")
    public String runAlgorithm() {
        algorithmService.runComplexAlgorithm();
        return "알고리즘 실행 완료!";
    }
}
