#include <iostream>
// An XOR linked list is a more memory efficient doubly linked list. Instead of
// each node holding next and prev fields, it holds a field named both, which is an
// XOR of the next node and the previous node. Implement an XOR linked list;
// it has an add(element) which adds the element to the end, and a get(index)
// which returns the node at index.
// If using a language that has no pointers (such as Python), you can assume you
// have access to get_pointer and dereference_pointer functions that converts
// between nodes and memory addresses.

// I had to consult a stackoverflow answer, this was so confusing.
// https://stackoverflow.com/questions/3531972/c-code-for-xor-linked-list

using namespace std;

struct Node {
    int data; // assuming the data type will be integer
    Node * both;
};

struct XORLinkedList {
    Node * head;
    Node * tail;
    long long size;

    static Node * XOR(Node * a, Node * b) {
        return (Node *) ((uintptr_t) (a) ^ (uintptr_t) (b));
    }

    void add(int element) {
        Node *node = new Node;
        node->data = element;
        node->both = tail;
        if (head == NULL) {
            head = node;
            tail = node;
        } else if (tail->both == NULL) {
            tail->both = node;
            //node->both = tail; already done at the top
        } else {
            tail->both = XOR(tail->both, node); 
        }

        tail = node;
        size++;
    }

    int get(int index) {
        Node *it;
        cout << tail->data << ' ' << head->data << endl;
        if (index >= (size / 2)) {
            cout << size << ' ' << index << endl;
            it = tail;
            Node * next = NULL;
            Node * prev;
            for (int i = (size - (index + 1)); i > 0; i--) {
                prev = XOR(it->both, next);
                next = it;
                it = prev;
            }
        }
        else {
            Node * prev = NULL;
            it = head;
            Node * next;
            for (int i = 0; i < index; i++) {
                next = XOR(prev, it->both);
                prev = it;
                it = next;
            }
        }
        return it->data;
    }
};

int main(void) {
    XORLinkedList new_list;
    new_list.add(0);
    new_list.add(1);
    new_list.add(2);
    new_list.add(3);
    new_list.add(4);
    cout << new_list.get(0) << " " << new_list.get(1) << " " << new_list.get(3) << " " << new_list.get(2) << " " << new_list.get(4) << endl;
    /* for some reason flshing more than once causes a segfault I can not figure out why for the life of me
    cout << new_list.get(2) << endl;
    cout << new_list.get(0) << endl; */
    return 0;
}
