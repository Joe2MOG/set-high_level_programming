#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject **items;

    if (!PyList_Check(p))
        return;

    /* Access ob_size directly (PyVarObject) */
    size = ((PyVarObject *)p)->ob_size;
    /* allocated is directly in PyListObject */
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    /* ob_item is the array of PyObject* */
    items = ((PyListObject *)p)->ob_item;
    for (i = 0; i < size; i++)
    {
        PyObject *item = items[i];
        /* Use ob_type field directly instead of Py_TYPE */
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    /* Get size via ob_size */
    size = ((PyVarObject *)p)->ob_size;
    /* Get the string buffer directly from the structure */
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size + 1 < 10 ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++)
        printf("%02x ", (unsigned char)str[i]);
    printf("\n");
}
