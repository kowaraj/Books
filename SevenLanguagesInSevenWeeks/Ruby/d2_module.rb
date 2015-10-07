module ToFi
  def fn
    "d2_filename_of_obj_#{self.object_id}.txt"
  end

  def to_f
    File.open(fn, 'w') {|f| f.write(method_get_name_of_someclass)}
  end
end  
  
