#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);

	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", alloc);

	int i = 0;
	PyObject *obj;

	for (i; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
