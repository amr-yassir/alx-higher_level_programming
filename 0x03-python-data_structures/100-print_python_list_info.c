#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
*/
void print_python_list_info(PyObject *p)
{
	int size, i;
	PyListObject *alloc;
	PyObject *obj;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);

	alloc = (PyListObject *)p;
	printf("[*] Allocated = %d\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
