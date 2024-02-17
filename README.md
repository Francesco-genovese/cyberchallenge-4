# cyberchallenge-4
# NOT WORKS CORRECTLY 

**Charlie:** Let me get this right: in binary exploitation, we inject massive strings into the program's input fields, and if we notice that our string is in memory where it shouldn't be, that's a problem, right?

**Alan:** Exactly, Charlie! And there's more: sometimes we need to carefully craft these strings to precisely locate our position within them.

**Bob:** Can't I just randomly mash the keyboard?

**Alan:** And what if you need thousands of characters?

**Bob:** Easy! I'll make them all the same and randomly change some at the end!

**Alan:** You might run into trouble with that, Bob... Typically, we resort to de Bruijn sequences, but that's a story for another time!

**Bob:** I'm not interested in that. My method always works in practice! I can prove it!

**Alan:** Alright, Bob, let's play: I give you a string S. How many strings R exist such that you can cover all of S using only copies of R?

**Bob:** The problem doesn't make sense; what do you mean by "cover"?

**Alan:** I mean that I can recreate the string S using copies of R, possibly overlapping them. For example, I can cover the string "xyxyxy" with "xy," "xyxy," and, of course, "xyxyxy" itself. Clear now?

**Bob:** Uh, yeah, it makes sense...

Alan takes a breath, hoping this leads to a momentary pause in Bob's enthusiasm...

**Problem Details:**

**Input:**
The input consists of 3T + 1 lines:

- *Line 1:* the number T of test cases you need to solve
- *Lines 2, ..., 3T + 1:* each group of 3 lines is formatted as follows:
  - *Line 1:* two integers separated by a space, N and M, respectively the length of the alphabet from which the string S is drawn and the length of the string S itself
  - *Line 2:* a string of length N, representing the alphabet
  - *Line 3:* a string of length M, the actual string S

**Output:**
The output consists of T lines, each representing the answer to the respective test case.

**Examples:**

**INPUT:**
```
3
2 11
SG GGGSGGSGSGG 24
PC
CCCC
26
HK
HKHKHK
1 4 3
```

**OUTPUT:**
```
1
4
3
```

**Explanation:**
The given input contains 3 distinct test cases:
- The first one, the string "GGGSGGSGSGG," can only be covered with the complete string itself.
- The second one, "CCCC," can be covered with "C," "CC," "CCC," or "CCCC."
- The third one, "HKHKHK," can be covered with "HK," "HKHK," or "HKHKHK."
