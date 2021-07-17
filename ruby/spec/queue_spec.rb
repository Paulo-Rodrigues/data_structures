require_relative '../lib/queue/queue'

describe Queue do
  subject(:queue) { Queue.new }

  it 'should be able to enqueue an item' do
    queue.enqueue(1)
    expect(queue.size).to eq(1)
  end

  it 'should be able to dequeue an item' do
    queue.enqueue(1)
    expect(queue.dequeue).to eq(1)
    expect(queue.size).to eq(0)
  end
end
