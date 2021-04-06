#include "stack.h"
#include <iostream>

using namespace std;

int main() {
  ItemType character;
  Stack stack;
  ItemType stackItem;

  cout << "Add a String " << endl;
  cin.get(charcter);
  while (character != '\n') {
    stack.push(charcter);
    cin.get(character);
  }

  while (!stack.isEmpty()) {
    stackItem = stack.pop();
    cout << stackItem;
  }
  cout << endl;
}
