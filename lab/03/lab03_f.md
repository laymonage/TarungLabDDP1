# Soal Tutorial

## Task Description

1. Your program should prompt for a **positive integer** in **decimal
   representation**, convert the integer to a **hexadecimal number string** and
   print it.
2. Then your program should prompt for a hexadecimal number string, convert the
   string into a regular decimal integer and print the result.

Here is a simple interaction:

```
>>>
Lab 03

From decimal to hexadecimal
---------------------------
Give a positive integer in decimal representation: 1027298
The hexadecimal representation of 1027298 is 0xface2

From hexadecimal to decimal
---------------------------
Give a positive integer in hexadecimal representation: 0xface2
The decimal representation of 0xface2 is 1027298

Thanks for using this program.

Press Enter to continue ...
```

## Hints

How do we get a hexadecimal string from a positive decimal integer? The
easiest method uses **integer division** by 16 on successive quotients and
then collects the **remainders**. It is best illustrated by an example.
Consider the decimal number 1564.

- 1564 divided by 16 gives the quotient 97 and remainder 12 (which is `c` in
  hexadecimal).
- 97 divided by 16 gives the quotient 6 and remainder 1.
- 6 divided by 16 gives the quotient 0 and remainder 6.

**Stop** at reaching a quotient of 0. The hexadecimal string equivalent is
given by concatenating the remainders, in reverse (so the last remainder is
the most significant digit and the first is the least).
In this example: "**61c**"

## Limitation

You are **not** allowed to use the Python function calls: `int(..., 16)` or
`hex(...)`.

Happy programming! 'Met ngoding!

L. Y. Stefanus

---

Taken from `lab03_fprog2017.pdf` (Tutorial Lab 3 DDP1 F -- 13 September 2017)
