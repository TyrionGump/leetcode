/*
 * @lc app=leetcode id=232 lang=java
 *
 * [232] Implement Queue using Stacks
 */

// @lc code=start

import java.util.Stack;

class MyQueue {

    private Stack<Integer> inStack = new Stack<>();
    private Stack<Integer> outStack = new Stack<>();

    public MyQueue() {
        
    }
    
    public void push(int x) {
        inStack.push(x);
    }
    
    public int pop() {
        while (!inStack.empty()) {
            outStack.push(inStack.pop());
        }

        int first = outStack.pop();

        while (!outStack.empty()) {
            inStack.push(outStack.pop());
        }

        return first;
    }
    
    public int peek() {
        while (!inStack.empty()) {
            outStack.push(inStack.pop());
        }

        int first = outStack.peek();

        while (!outStack.empty()) {
            inStack.push(outStack.pop());
        }

        return first;
    }
    
    
    public boolean empty() {
        return inStack.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
// @lc code=end

