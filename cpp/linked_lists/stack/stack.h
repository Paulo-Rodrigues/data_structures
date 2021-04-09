#include "node.h"

class Stack {
  public:
    Stack();
    ~Stack();
    
    bool isEmpty() const;
    bool isFull() const;
    bool print() const;

    void push(ItemType);
    ItemType pop();

  private:
    Node* structure;
};
