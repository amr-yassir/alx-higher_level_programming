#include <stdio.h>
#include <python.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc;
	PyObject *obj;

	size = py_size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	int i = 0;

	for (i; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
