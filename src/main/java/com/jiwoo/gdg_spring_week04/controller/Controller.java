package com.jiwoo.gdg_spring_week04.controller;

import com.jiwoo.gdg_spring_week04.service.SampleClass;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/sample")
public class Controller {

    @Autowired
    private SampleClass sampleClass;

    @GetMapping("/serve")
    public String serve() throws InterruptedException{
        sampleClass.serve();
        return "Service excuted";
    }
}
