#include <stdio.h>
#include <Python.h>
#include <object.h>
#include<listobject.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Object
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %d bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Object
 */
void print_python_list(PyObject *p)
{
	int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
