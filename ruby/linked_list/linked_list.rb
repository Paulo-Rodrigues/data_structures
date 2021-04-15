require_relative './node'

class LinkedList
  def initialize
    @head = nil
    @tails = nil
  end

  def push(value)
    this_node = Node.new(value)
    if @head.nil?
      @head = this_node
      return
    end

    current = @head

    until current.next.nil?
      current = current.next
    end

    current = this_node
  end

  def remove(index)
    if @head.nil?
      puts 'empty'
    end

    if index == 0
      current = @head
      new_current = current.next
      @head = new_current
    end

    if index > 0
      current = get_node(index)
      previous_node = get_node(index-1)
      posterior_node = current.next
      previous_node.next = posterior_node
    end
  end

  private

  def get_node(index)
    current = @head
    index.times do
      current = current.next
    end
    return current
  end
end
