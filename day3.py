# Python Calculator Extension Module

This project demonstrates how to create a Python extension module in C for a simple calculator with basic arithmetic functions. The module provides functions for addition, subtraction, multiplication, and division.

## Prerequisites

- Python development headers
- GCC compiler
- Make utility

### Installing Python Development Headers

For Debian-based systems (Ubuntu, etc.):
```sh
sudo apt-get update
sudo apt-get install python3-dev
####################################################### 


#include <Python.h>

// Function to add two numbers
static PyObject* py_add(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("d", a + b);
}

// Function to subtract two numbers
static PyObject* py_subtract(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("d", a - b);
}

// Function to multiply two numbers
static PyObject* py_multiply(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("d", a * b);
}

// Function to divide two numbers
static PyObject* py_divide(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    if (b == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero");
        return NULL;
    }
    return Py_BuildValue("d", a / b);
}

// Method definitions
static PyMethodDef CalculatorMethods[] = {
    {"add", py_add, METH_VARARGS, "Add two numbers"},
    {"subtract", py_subtract, METH_VARARGS, "Subtract two numbers"},
    {"multiply", py_multiply, METH_VARARGS, "Multiply two numbers"},
    {"divide", py_divide, METH_VARARGS, "Divide two numbers"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef calculatormodule = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    NULL,
    -1,
    CalculatorMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculatormodule);
}
###########################################################################################################################

#makefile

CC = gcc
RM = rm

CFLAGS = -O2 -Wall -c

OUTPUT_DIR = bin
OBJ_DIR = obj

TARGET_LIB = $(OUTPUT_DIR)/calculator

INCLUDES = \
    -I/usr/include/python3.11  # Update to your Python version

LIB_SRCS = calculator.c
LIB_OBJS  = $(LIB_SRCS:%.c=$(OBJ_DIR)/%.o)

.PHONY: all
all: $(TARGET_LIB)

$(TARGET_LIB): $(LIB_OBJS)
	mkdir -p $(dir $@)
	$(CC) -shared $^ $(INCLUDES) -o $@.so

$(OBJ_DIR)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCLUDES) $< -o $@

.PHONY: clean
clean:
	-$(RM) -rf $(OUTPUT_DIR)/* $(OBJ_DIR)/*
###############################################################################################################################

#example program

# test_calculator.py

import sys
sys.path.append('./bin')  # Add the path to the shared library

import calculator

print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(5, 3))
print("Multiplication:", calculator.multiply(5, 3))
print("Division:", calculator.divide(5, 3))
##############################################################################################################################
