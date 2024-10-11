package hello.hello_spring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {
    @GetMapping("hello")
    public String hello(Model model){
        model.addAttribute( "data", "spring!");
        return "hello";
    }

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name,Model model) {
        model.addAttribute("name",name);
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody  //body를 직접 내려주겠다(view같은거 없이 문자가 바로 내려감)
    public String helloString(@RequestParam("name") String name){
        return "hello "+ name; //hello spring
    }

    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name){
        Hello hello = new Hello();
        hello.setName(name);
        return hello;  //문자가 아닌 객체를 리턴
    }
    //클래스 만듬
    static class Hello{
        private String name;
        public String getName(){
            return name;
        }
        public void setName(String name){
            this.name = name;
        }
    }


}
