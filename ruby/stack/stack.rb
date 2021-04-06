class Stack
  attr_acccessor :items

  def initialize
    @items = []
  end

  def empty?
    items.empty?
  end

  def push(item)
    items << item
  end

  def pop
    items.pop
  end

  def peek
    items.last
  end
end
