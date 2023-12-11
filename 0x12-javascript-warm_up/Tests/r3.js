/*
Resource-3: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures

Primitive values:
------------------
- all types except Object define immutable values.
- all primitive types except null, can be tested by the typeof operator.

DataTypes:
----------
Null-object-N/A
Undefined-undefined-N/A
Boolean-boolean-Boolean
Number-number-Number
BigInt-number-BigInt
String-string-String
Symbol-symbol-Symbol
*/

const x = BigInt(Number.MAX_SAFE_INTEGER);
x + 1n === x + 2n;

Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2;

// This resource is incomplete, Continue starting from NUll type.
