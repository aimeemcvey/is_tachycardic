# Unit Testing and Continuous Integration
Function that could be used to interpret whether a string obtained from OCR of medical records contains the word "tachycardic".

The function is named ```is_tachycardic``` and is located in a module ```tachycardia.py```. This function takes a string argument as an input and returns ```True``` if the input is "tachycardic", allowing for upper, lower, or mixed case inputs as well as leading/trailing spaces, punctuation, and slight misspellings. If the input is another word, the function returns ```False```.

The ```test_tachycardia.py ``` module contains unit tests for this feature.
