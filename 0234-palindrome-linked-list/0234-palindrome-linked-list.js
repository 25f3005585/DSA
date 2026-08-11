/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
const isPalindrome = function(head) {
    if (!head || !head.next) return true;
    const reverseRecursively = (node) => {
        if (node === null || node.next === null) {
            return node;
        }
        const newHead = reverseRecursively(node.next);
        node.next.next = node;
        node.next = null;
        return newHead;
    };

    let slow = head;
    let fast = head;
    
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let reversedHalf = reverseRecursively(slow);

    let firstHalf = head;
    let secondHalf = reversedHalf;

    while (secondHalf) {
        if (firstHalf.val !== secondHalf.val) {
            return false;
        }
        firstHalf = firstHalf.next;
        secondHalf = secondHalf.next;
    }

    return true;
};
