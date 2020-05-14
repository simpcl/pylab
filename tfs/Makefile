
TARGET=tfs.so
OBJS=tfs.o
CC=gcc
PYTHON_INC=/opt/python-2.7.18/include/python2.7/
CFLAGS=-fpic -c -I $(PYTHON_INC)

all: $(OBJS)
	$(CC) -shared -o $(TARGET) $(OBJS)

tfs.o: tfs.c
	$(CC) -o tfs.o $(CFLAGS) tfs.c

clean:
	rm -f $(OBJS) $(TARGET) *.pyc

