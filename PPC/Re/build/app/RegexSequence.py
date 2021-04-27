class RegexSequence:
    def __init__(self, string_sequence, regex_sequence):
        """
        :param string_sequence: The string this object corresponds to, ie ab
        :param regex_sequence:  String, representing the current state of object's regex, ie '[aq|cs|ab]'
        """
        self.text_sequence = string_sequence
        self.regex_sequence = regex_sequence
