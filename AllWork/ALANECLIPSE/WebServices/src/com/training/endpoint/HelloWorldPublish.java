package com.training.endpoint;

import javax.xml.ws.Endpoint;
import com.training.ws.HelloWorldImpl;


public class HelloWorldPublish {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Endpoint.publish("http://localhost:9000/ws/hello", new HelloWorldImpl());


	}

}
