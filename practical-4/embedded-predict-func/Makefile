CC = gcc
CFLAGS = -std=c99 -pedantic -Wall -Werror -Wextra -Wvla

SRCS = ml_func.c
OBJS = $(patsubst %.c, %.o, $(SRCS))
TARGET = libml.a

all: $(TARGET)

$(TARGET): $(OBJS)
	ar csr $@ $(OBJS)

%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS) $(TARGET)
