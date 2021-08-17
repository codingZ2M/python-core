
class SuperList(list):   # Passing 'list' as parent class to our user defined 'SuperList' class
  def __len__(self):
    return 1000

super_list1 = SuperList();

#print(len(super_list1))
print(super_list1.__len__())

super_list1.append(5)
print(super_list1[0]) # Extending the functionality of list

print(issubclass(list, object))