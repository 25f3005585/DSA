/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

class Stack {
    constructor() {
        this.stack = [];
    }

    push(value) {
        this.stack.push(value);
    }

    pop() {
        return this.stack.pop();
    }

    peek() {
        return this.stack[this.stack.length - 1];
    }

    isEmpty() {
        return this.stack.length === 0;
    }
}

const backspaceCompare = function (s, t) {
    const stack1 = new Stack()
    for (let i = 0; i < s.length; i++) {
        const element = s[i]
        if (stack1.isEmpty() && element !== "#") {
            stack1.push(element)
        } else if (element === "#") {
            stack1.pop()
        } else {
            stack1.push(element)
        }
    }
    const stack2 = new Stack()
    for (let i = 0; i < t.length; i++) {
        const element = t[i]
        if (stack2.isEmpty() && element !== "#") {
            stack2.push(element)
        } else if (element === "#") {
            stack2.pop()
        } else {
            stack2.push(element)
        }
    }

    const string1 = (stack1.stack || []).join('');
    const string2 = (stack2.stack || []).join('');
    return string1 === string2;
};