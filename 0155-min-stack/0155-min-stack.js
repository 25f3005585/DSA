class MinStack {
    constructor() {
        this.stack = [];
        this.minimum = Infinity;
    }

    push(value) {
        this.stack.push(value);
        this.minimum = Math.min(value, this.minimum);
    }

    pop() {
        const element = this.stack.pop();
        if (element === this.minimum) {
            this.minimum = Infinity;
            for (let i = this.stack.length - 1; i >= 0; i--) {
                this.minimum = Math.min(this.minimum, this.stack[i]);
            }
        } else {
            return this.minimum;
        }
    }

    getMin() {
        return this.minimum;
    }

    top() {
        return this.stack[this.stack.length - 1];
    }
}
