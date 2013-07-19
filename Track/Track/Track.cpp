// Track.cpp : Defines the entry point for the console application.
// Author: Pranav Shenoy
// July 2013
/*
#include <Python.h>

int main (int argc, char *argv[]){
	Py_SetProgramName(argv[0]);
	Py_Initialize();
	PyRun_SimpleString("from time import time, ctime\nprint 'Todayis ',ctime(time())\n");
	Py_Finalize();
	return 0;
}

*/
#include <Python.h>
#include "stdafx.h"
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    PyObject *pName, *pModule, *pDict, *pFuncOne, *pValue;
	PyObject *pArgs;
	PyObject *pFuncTwo;

    if (argc < 3) 
    {
//		for (int i = 0; i < 500000; i++){
			printf("ONZZ - Usage: exe_name python_source function_name\n");
//		}
//        return 1;
    }

    // Initialize the Python Interpreter
    Py_Initialize();

	//FILE:
	//********************
    // Build name object
    pName = PyString_FromString("py_function");
    // Load module 
    pModule = PyImport_Import(pName);
	Py_DECREF(pName);
    // borrowed reference 
    pDict = PyModule_GetDict(pModule);

	//FUNCTION:
	//********************
    // borrowed reference 
	pFuncOne = PyObject_GetAttrString(pModule, "multiply");
	// borrowed ref
	pFuncTwo = PyObject_GetAttrString(pModule, "test");


    if (PyCallable_Check(pFuncOne)) 
    {
        PyObject_CallObject(pFuncOne, NULL);
    } else 
    {
		cout << "pranav, you suck at this";
        PyErr_Print();
    }

	if (PyCallable_Check(pFuncOne)) 
    {
        PyObject_CallObject(pFuncTwo, NULL);
    } else 
    {
		cout << "pranav, you suck at this?";
        PyErr_Print();
    }


    // Clean up
    Py_DECREF(pModule);
    Py_DECREF(pName);
    // Finish the Python Interpreter
		for (int i = 0; i < 5000; i++){
			printf("Func\n");
		}

    Py_Finalize();

    return 0;
}
