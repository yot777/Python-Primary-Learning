package com.yty.test6;

import com.yty.test5.A;

public class B {
	public void B(){
		System.out.println("This is init function of B");			
	}
	public static void main(String[] args) {
		//������A��֮�󣬱���ʵ����һ��A��Ķ���a�����ܵ���A��ķ���
		A a = new A();
		a.A();
		B b = new B();
		b.B();
	}
}
