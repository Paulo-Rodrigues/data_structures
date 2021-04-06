class Queue
  attr_accessor :items

  def initialize
    @items = []
  end

  def front
    items.first
  end

  def back
    items.last
  end

  def empty?
    items.empty?
  end

  def enqueue(item)
    items << item
  end

  def dequeue
    items.delete_at(0)
  end
end
