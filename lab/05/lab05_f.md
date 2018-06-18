# Soal Tutorial

1. An *acronym* is a word formed by taking the first letters of the words in a
   phrase and then making a word from them. For example, RAM is an acronym for
   **random access memory**.

   Write a function `acronym()` that takes a phrase (i.e., a string) as input
   and then **returns** the acronym for that phrase. The acronym should be all
   **uppercase**, even if the words in the phrase are not capitalized.

   For examples:

   ```python
   >>> acronym('Random Access Memory')
   'RAM'
   >>> result = acronym('Central processing unit')
   >>> result
   'CPU'
   >>> print(result)
   CPU
   ```

   In this function we iterate over the words of the phrase and *accumulate*
   the first letter in every word. So we need to break the phrase into a list
   of words and then iterate over the words in this list.

   The string method `split` generates a list of strings by splitting the
   original string at certain separators such as spaces. For example:

   ```python
   >>> split_list = 'this is a test'.split()
   >>> split_list
   ['this', 'is', 'a', 'test']
   ```

   ```python
   # function template
   def acronym(phrase):
       .
       .
       .
       return ...
   ```

   Test your function in IDLE.

2. Copy the textfile `phrases.txt` to your working directory. This file will be
   used for testing.

3. Construct a complete Python program which uses the function `acronym()`
   from Part 1 above for finding the acronym of each phrase in an existing
   text-file and write the result to a new text file. Your program prompts the
   user for an input file name and an output file name. Test your program on
   the file `phrases.txt`. Your program should validate the file names entered
   by the user. Your program should keep asking for a file name until the user
   gets it right.

   To avoid accidentally over writing (erasing) an existing file, open a new
   file for writing with mode `'x'` instead of `'w'`. If an existing file is
   opened for writing with mode `'x'`, exception `FileExistsError` will be
   raised. Your program should handle this exception by asking for another
   file name. Your program should also handle exception `KeyboardInterrupt`.

   Sample user interaction: (user's responses are in *italic*)

   <pre>

   Please enter input file name: *depok.txt*
   The file depok.txt doesn't exist.
   Try again.

   Please enter input file name: #user type Ctrl-C
   Keyboard Interrupt. Input file is required.

   Please enter input file name: *phrases.txt*

   Please enter output file name: *phrases.txt*
   The file phrases.txt already exists.
   To avoid overwriting an existing file, try anoth file name.

   Please enter output file name: *newFile.txt*
   End of the program. Please type Enter to finish... 

   </pre>

   For example, if the input file contains:

   ```
   Always And Forever
   All Done Bye Bye
   As far as I 
   remember
   Random Access Memory
   Central processing unit
   Keep it simple, students!
   ```

   then the output file will contain:

   ```
   AAF = Always And Forever
   ADBB = All Done Bye Bye
   AFAIR = As far as I remember
   RAM = Random Access Memory
   CPU = Central processing unit
   KISS = Keep it simple, students!
   ```

   You can follow the following program template:

   ```python
   def acronym(phrase):
       .
       .
       .
       return result

   def main()
       # User provides both the input file and the output file name.
       # Use exceptions to validate input.
       # get file name and try to open the file
       # keep prompting user until a correct file name is given
       .
       .
       .
       # hold the screen if program is run outside IDLE
       input("End of the program. Please type Enter to finish...")

   main()
   ```

Happy programming! 'Met ngoding!

L. Y. Stefanus

---

Taken from `lab04_fprog2017.pdf` (Tutorial Lab 4 DDP1 F -- 6 October 2017)
