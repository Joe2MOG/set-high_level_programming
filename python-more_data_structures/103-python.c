#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: PyObject pointer to a bytes object
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		printf("  first 10 bytes: ");
	else
		printf("  first %ld bytes: ", size + 1);

	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02x", str[i] & 0xff);
		if (i == size || i == 9)
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - prints basic info about Python list objects
 * @p: PyObject pointer to a list object
 */
void print_python_list(PyObject *p)
{
	long int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;

	size = ((PyVarObject *)p)->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}
