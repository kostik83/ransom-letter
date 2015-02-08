def hasSuffiecentCharacters(newspaperClipping, ransomLetter):
    found = {}
    cnt = 0

    if len(ransomLetter) > len(newspaperClipping):
        return False
    
    for letter in ransomLetter:
        if letter.isspace():
            continue

        #lets make all lowercase, we don't care about case
        ch = ord(letter)
        if ch >= 65 and ch <= 90:
            letter = chr(ch + 32)

        if letter in found:
            found[letter] -= 1
            if found[letter] == 0:
                del found[letter]
        else:
            for s in newspaperClipping[cnt:]:
                cnt += 1
                if s.isspace():
                    continue

                ch = ord(s)
                if ch >= 65 and ch <= 90:
                    s = chr(ch + 32)

                if s == letter:
                    # found needed letter
                    break;
                else:
                    # add to found dictionary
                    if s in found:
                        found[s] += 1
                    else:
                        found[s] = 1
            else:
                # we reached the end of clipping
                return False;
    
    # we reached end of letter
    return True;

   
ransomLetter = 'I have your code, please give me github access to get it back'

newspaperClipping = '''
Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale.

Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.

Python interpreters are available for installation on many operating systems, allowing Python code execution on a wide variety of systems. Using third-party tools, such as Py2exe or Pyinstaller, Python code can be packaged into stand-alone executable programs for some of the most popular operating systems, allowing for the distribution of Python-based software for use on those environments without requiring the installation of a Python interpreter.
'''

result = hasSuffiecentCharacters(newspaperClipping, ransomLetter)

print(result)