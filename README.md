# 55words
A simple validator for 55-word fiction challenges.

This script counts the words in a blob of text according to the official "55 words" ruleset from the [New Times San Luis Obispo](https://www.newtimesslo.com/sanluisobispo/55FictionHowtoEnter/Page):

* You can write about anything you like, but you can't use more than 55 words. Yes, you can use fewer if you'd like to, but we don't know why anyone would. Don't shortchange yourself even more than we already have.
* And what, exactly, is a word? Simple. If it's in the dictionary, it's a word.
* Hyphenated words can't count as single words. For example, "blue-green dress" is three words, not two. Exceptions to this are any words that don't become two complete free-standing words when the hyphen is removed, like "re-entry."
* Also, please note that your story's title isn't included in the word count. But remember that it can't be more than seven words long.
* Contractions count as single words, so if you're really seeking word economy (as you should be), keep this in mind. If you write, "He will jump," it's three words. But if you write, "He'll jump," it's only two. Very economical. By the same token, any contraction that's a shortened form of a word is also counted as a full word. Like using "'em" for "them."
*  An initial also counts as a word (L.L. Bean, e.e. cummings, etc.) since it's basically an abbreviation of a full word. The only exception is when it's part of an acronym like MGM, NASA, or IBM. The reasoning here is that the wide use of these acronyms has in effect made them into single words.
*  Remember that numbers count as words, too, expressed as either numerals (8, 28, 500, or 1984), or as words (eight, twenty-eight, etc.). But keep in mind our hyphenated-word rule. "Twenty-eight" is two words when written out, but only one when expressed as 28. Don't cheat yourself out of an extra word that you may need.
*  Any punctuation is allowed, and no punctuation marks count as words, so don't worry about being miserly with them if they work to some effect.

## Usage
The script takes in raw text from the console and spits out the word count. Simple.

Pipe any text into stdin:

`./55words.py < mystory.txt`

## Example
Note: I am including the (famous) example story "Bedtime" by Jeffrey Whitmore from the New Times San Luis Obispo website as text here. All rights belong to the author.

```
» ./55words.py < example.txt
Body word count: 54 (limit is 55 words)
```

## Acknowledgments
I used chatgpt to write some of this code.
