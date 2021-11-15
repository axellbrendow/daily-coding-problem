/*
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding
next and prev fields, it holds a field named both, which is an XOR of the next node and the
previous node. Implement an XOR linked list; it has an add(element) which adds the element to
the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to
get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
*/

#include <cassert>

class Node {
public:
	int val;
	Node *both = nullptr;

	Node(int val, Node *both) : val(val), both(both) {}
};

class LinkedList {
public:
	Node *head;

	LinkedList() : head(new Node(0, nullptr)) {}

	Node *xorNodes(Node *prev, Node *currBoth) {
		return reinterpret_cast<Node*>(
			reinterpret_cast<long>(prev)
			^ reinterpret_cast<long>(currBoth)
		);
	}

	void add(int val) {
		// head -> 2 -> 3 ->
		//      <-   <- 
		Node *prev = head;
		Node *curr = prev->both;
		while (curr != nullptr) {
			Node *temp = prev;
			prev = curr;
			curr = xorNodes(temp, curr->both);
		}
		Node *newNode = new Node(val, prev);
		prev->both = xorNodes(prev->both, newNode);
	}

	Node *get(int index) {
		if (index < 0) return nullptr;
		Node *prev = head;
		Node *curr = prev->both;
		while (curr != nullptr && index > 0) {
			Node *temp = prev;
			prev = curr;
			curr = xorNodes(temp, curr->both);
			index--;
		}
		return index == 0 ? curr : nullptr;
	}
};

int main() {
	LinkedList list;
	list.add(7);
	list.add(2);
	list.add(3);
	list.add(5);
	assert(list.get(0)->val == 7);
	assert(list.get(1)->val == 2);
	assert(list.get(2)->val == 3);
	assert(list.get(3)->val == 5);
}
