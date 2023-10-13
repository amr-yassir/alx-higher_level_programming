#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints python list info
 * @p: PyObject
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);

	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
