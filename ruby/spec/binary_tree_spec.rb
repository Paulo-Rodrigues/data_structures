require_relative '../lib/trees/binary_tree/binary_tree'

describe BinaryTree do
    let(:tree) { BinaryTree.new(5) }
    
    it "should insert values" do
        tree.insert(3)
        
        expect(tree.left.value).to eq(3)
    end

    it "should search values" do
        tree.insert(3)
        
        expect(tree.search(3)).to eq(true)
    end
end