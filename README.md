<h1>PLY-Based Python Syntax Parser</h1>

This project demonstrates the use of the PLY (Python Lex-Yacc) library to build lexical analyzers and parsers for a subset of Python constructs. It features:

<ul>
  <li>Syntax validation for function definitions</li>
  <li>Parsing for control structures (if/else, for, while)</li>
  <li>Support for list declarations</li>
</ul>

<h2>Features</h2>
<ul>
  <li>Function declaration parsing</li>
  <li>If and If-Else conditional parsing</li>
  <li>For loop parsing (including range variations)</li>
  <li>While loop parsing with logical expressions</li>
  <li>List declaration parsing with support for integers, floats, and strings</li>
  <li>Error handling for invalid syntax and tokens</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>PLY library (<code>pip install ply</code>)</li>
</ul>

<h2>How to Run</h2>
<ol>
  <li>Install Python 3.x and the PLY library (<code>pip install ply</code>).</li>
  <li>Clone or download the project files.</li>
  <li>Run any parser script (e.g., <code>python function_parser.py</code>).</li>
  <li>Enter a code snippet when prompted to validate its syntax.</li>
</ol>

<h2>Files</h2>
<ul>
  <li><b>function_parser.py</b>: Parser for function declarations</li>
  <li><b>if_else_parser.py</b>: Parser for if and if-else conditionals</li>
  <li><b>for_loop_parser.py</b>: Parser for for loops</li>
  <li><b>while_loop_parser.py</b>: Parser for while loops</li>
  <li><b>list_parser.py</b>: Parser for list declarations</li>
</ul>

<h2>Notes</h2>
<ul>
  <li>This project is developed for educational purposes as part of AFLL coursework.</li>
  <li>Each parser handles a specific subset of Python syntax.</li>
</ul>

<h2>License</h2>
This project is licensed under the MIT License.
