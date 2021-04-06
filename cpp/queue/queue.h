#include "item_type.h"
const int MAX_ITEMS = 100;

class Queue {
  public:
    Queue();
    ~Queue();
    bool isFull() const;
    bool isEmpty() const;
    void print() const;

    void enqueue(ItemType);
    ItemType dequeue();

  private:
    int front;
    int back;
    ItemType* structure;
}
