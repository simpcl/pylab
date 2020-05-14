#include <Python.h>

#include "crc32.h"

#define Byte char
PyObject* crc32_wrapper(PyObject* self, PyObject* args)
{
  unsigned int crc32val = 0;  /* crc32(0L, Z_NULL, 0) */
  Py_buffer pbuf;
  Byte *buf;
  Py_ssize_t len;
  int signed_val;

  if (!PyArg_ParseTuple(args, "s*|I:crc32", &pbuf, &crc32val))
    return NULL;
  buf = (Byte*)pbuf.buf;
  len = pbuf.len;
  signed_val = tfs_crc32(crc32val, buf, len);
  PyBuffer_Release(&pbuf);
  return PyInt_FromLong(signed_val);
}

static PyMethodDef tfsMethods[] = 
{
  {"crc32", crc32_wrapper, METH_VARARGS, "CRC32 For TFS File Content"},
  {NULL, NULL}
};

void inittfs() 
{
  PyObject* m;
  m = Py_InitModule("tfs", tfsMethods);
}

