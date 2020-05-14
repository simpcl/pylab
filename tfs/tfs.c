#include <Python.h>

#include "crc32.h"
#include "fsname.h"

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

PyObject* encode_fsname_wrapper(PyObject* self, PyObject* args)
{
  long app_id;
  long long file_id;

  if (!PyArg_ParseTuple(args, "il", &app_id, &file_id))
    return NULL;

  const char* fsname = encode_fsname((uint32_t)app_id, (uint64_t)file_id);
  if (!fsname) {
    return NULL;
  }

  return Py_BuildValue("s", fsname);
}

PyObject* decode_fsname_wrapper(PyObject* self, PyObject* args)
{
  Py_buffer pbuf;
  Byte *buf;
  Py_ssize_t len;
  filebits_t filebits;

  if (!PyArg_ParseTuple(args, "s*", &pbuf))
    return NULL;
  buf = (Byte*)pbuf.buf;
  len = pbuf.len;

  int ret = decode_fsname(buf, len, &filebits);
  if (ret < 0) {
    return NULL;
  } 

  PyBuffer_Release(&pbuf);

  return Py_BuildValue("il", filebits.app_id, filebits.file_id);
}

static PyMethodDef tfsMethods[] = 
{
  {"crc32", crc32_wrapper, METH_VARARGS, "CRC32 For TFS File Content"},
  {"encode_fsname", encode_fsname_wrapper, METH_VARARGS, "Encode Fsname According TFS"},
  {"decode_fsname", decode_fsname_wrapper, METH_VARARGS, "Decode Fsname According TFS"},
  {NULL, NULL}
};

void inittfs() 
{
  PyObject* m;
  m = Py_InitModule("tfs", tfsMethods);
}

