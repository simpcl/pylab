
TARGET=tfs.so
OBJS=tfs.o crc32.o
CC=gcc
PYTHON_INC=/opt/python-2.7.18/include/python2.7/
#CFLAGS=-fpic -c -I $(PYTHON_INC)
CFLAGS=-Wall -g -c -O0 -fPIC -I $(PYTHON_INC)

all: $(OBJS)
	$(CC) -shared -o $(TARGET) $(OBJS)

#tfs.o: tfs.c
#	$(CC) -o tfs.o $(CFLAGS) tfs.c
$(OBJS): %o:%c
	$(CC) $(INCS) -c $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJS) $(TARGET) *.pyc

