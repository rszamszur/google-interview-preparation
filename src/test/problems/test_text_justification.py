import pytest
from dsa.problems.text_justification import text_justification


@pytest.mark.parametrize("words, max_width, expected", [
    (
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        ["This    is    an","example  of text","justification.  "],
    ),
    (
        ["What","must","be","acknowledgment","shall","be"],
        16,
        ["What   must   be","acknowledgment  ","shall be        "],
    ),
    (
        ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
        20,
        ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "],
    ),
])
def test_text_justification(words, max_width, expected):
    assert text_justification(words, max_width) == expected
