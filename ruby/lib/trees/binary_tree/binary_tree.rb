class BinaryTree
    attr_reader :value
    attr_accessor :left, :right

    def initialize(value)
        @value = value
        @left = nil
        @right = nil
    end
    
    def insert(value)
        if value <= @value
            if @left.nil?
                @left = BinaryTree.new(value)
            else
                @left.insert(value)
            end
        else
            if @right.nil?
                @right = BinaryTree.new(value)
            else
                @right.insert(value)
            end
        end
    end

    def search(value)
        if value == @value
            return true
        elsif value < @value
            return @left.search(value) if @left
        else
            return @right.search(value) if @right
        end
    end
end
