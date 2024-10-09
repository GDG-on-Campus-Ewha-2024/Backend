package com.jiwoo.gdg_spring_week04.service;

import com.jiwoo.gdg_spring_week04.aspect.LogExecutionTime;
import org.springframework.stereotype.Component;

@Component
public class SampleClass {

    @LogExecutionTime
    public void serve() throws InterruptedException{
        Thread.sleep(2000);
    }
}
