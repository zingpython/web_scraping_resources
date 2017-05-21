Learn Regular Expressions


```
http://pythex.org
```
Phone numbers:
```
000-000-0000
```
```
000 000 0000
```
```
000.000.0000
```
```
(000)000-0000
```
```
(000)000 0000
```
```
(000)000.0000
```
```
(000) 000-0000
```
```
(000) 000 0000
```
```
(000) 000.0000
```
```
0000000
```
```
0000000000
```
```
(000)0000000
```

This is the process of building a phone number scraping regex.

First, we need to match an area code (3 digits), a trunk (3 digits), and an extension (4 digits):
```
reg = re.compile("\d{3}\d{3}\d{4}")
```
Now, we want to capture the matched phone number, so we add parenthesis around the parts that we're interested in capturing (all of it):
```
reg = re.compile("(\d{3}\d{3}\d{4})")
```

Now, the phone number might actually start with a ( character (if the area code is enclosed in parentheses):
```
reg = re.compile("(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?")
```


```
'.'
```
(Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.
```
'^'
```
(Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
```
'$'
```
Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline. foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches only ‘foo’. More interestingly, searching for foo.$ in 'foo1\nfoo2\n' matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode; searching for a single $ in 'foo\n' will find two (empty) matches: one just before the newline, and one at the end of the string.
```
'*'
```
Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
```
'+'
```
Causes the resulting RE to match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
```
'?'
```
Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.
```
*?, +?, ??
```
The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE <.*> is matched against <a> b <c>, it will match the entire string, and not just <a>. Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. Using the RE <.*?> will match only <a>.
```
{m}
```
Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match. For example, a{6} will match exactly six 'a' characters, but not five.
```
{m,n}
```
Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible. For example, a{3,5} will match from 3 to 5 'a' characters. Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound. As an example, a{4,}b will match aaaab or a thousand 'a' characters followed by a b, but not aaab. The comma may not be omitted or the modifier would be confused with the previously described form.
```
{m,n}?
```
Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible. This is the non-greedy version of the previous qualifier. For example, on the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, while a{3,5}? will only match 3 characters.
```
'\'
```
Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence; special sequences are discussed below.

If you’re not using a raw string to express the pattern, remember that Python also uses the backslash as an escape sequence in string literals; if the escape sequence isn’t recognized by Python’s parser, the backslash and subsequent character are included in the resulting string. However, if Python would recognize the resulting sequence, the backslash should be repeated twice. This is complicated and hard to understand, so it’s highly recommended that you use raw strings for all but the simplest expressions.