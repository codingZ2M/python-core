# *args and **kwargs

# Passing any number of positional arguments using (*args)
def compute(*args):

    print(args)          # args inside of the function is a Tuple
    return sum(args)

result = compute(1,2,3,4,5)
print(result)
print()


# Keyword Args (**kwargs) In-order to fetch any number of keyword arguments

# Order Rule: params, *args, default parameters, **kwargs
def employeeDetails(name, *args, id=1011,  **kwargs):
    print(f'Name: {name}')
    print(f'Employee Id: {id}')
    for project in args:
        print(f'Project: {project}')
    for projectId in kwargs.values():
        print(f'ProjectId: {projectId}')

employeeDetails('Rick', 'Java', 'Python',  projectId1=11, projectId2=12)



