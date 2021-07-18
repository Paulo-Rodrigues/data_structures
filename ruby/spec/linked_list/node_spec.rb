require_relative '../../lib/linked_list/node'

describe Node do
    it "should be able to create a node" do
      node = Node.new(1)
      node.value.should == 1
    end
  
    it "should be able to create a node with a next" do
      node = Node.new(1)
      node.next = Node.new(2)
      node.next.value.should == 2
    end
  end