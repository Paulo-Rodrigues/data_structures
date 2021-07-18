require_relative '../lib/stack/stack'

describe Stack do
    let(:stack) { Stack.new }
  
    it 'should be empty' do
      expect(stack.empty?).to be_truthy
    end
  
    it 'should be able to push an item' do
      stack.push(:foo)
      expect(stack.peek).to eq(:foo)
    end
  
    it 'should be able to pop an item' do
      stack.push(:foo)
      stack.pop
      expect(stack.empty?).to be_truthy
    end
  
    it 'should be able to peek at the last item' do
      stack.push(:foo)
      expect(stack.peek).to eq(:foo)
    end
  end
  