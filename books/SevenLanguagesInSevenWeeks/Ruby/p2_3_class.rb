class Tree
  #attr_accessor :children, :node_name
  def initialize(name, children=[]) @children = children
    @node_name = name
  end

  def visit_all(&block)
    visit &block
    children.each {|c| c.visit_all &block}
  end
  
  def visit_all()
    puts "I am %s" % self.node_name
    children.each {|c| c.visit_all}
  end

  def visit(&block) block.call self
  end

  def add_node(name)
    new_tree = Tree.new(name)
    children.insert(0, new_tree)
  end

  def add_node(tree)
    children.insert(0, tree)
  end
end

