class RegexGeneratorsFactory:
    """
    Factory for generators. Use this to handle regex generations.
    """
    def __init__(self):
        self.generators = [NoopRegexGenerator, CharacterSetGenerator, AlternationGenerator]

    def get_generator(self, generator_name):
        return self.generators[generator_name]

    def __getitem__(self, key):
        return self.generators[key]()

    def __len__(self):
        return len(self.generators)


class NoopRegexGenerator:
    """
    The trivial regex generator.
    """
    def get_regex(self, match_symbols, dont_match_symbols):
        return match_symbols

class CharacterSetGenerator:
    """
    Generator that transforms plaintext into charset, ie ab => [aqdmb] or ab => [^cdmfd]
    """
    def get_regex(self, match_symbols, dont_match_symbols, negate=False):
        return self._generate_regex(match_symbols, dont_match_symbols, negate)

    def _generate_regex(self, match_symbols, dont_match_symbols, negate=False):
        if not negate:
            generated_regex = '[' + ''.join(match_symbols) + ']+'
        else:
            generated_regex = '[^' + ''.join(dont_match_symbols) + ']+'
        return generated_regex

class AlternationGenerator:
    """
    Generator that transforms plaintext alternation, ie ab => ab|cs|fm
    """
    def get_regex(self, match_symbols):
        """
        :param match_symbols: list of iterables of sequences to match, ie [['ab'], ['cd']...]
        """
        return self._generate_regex(match_symbols)

    def _generate_regex(self, match_symbols, dont_match_symbols=[]):
        generated_regex = '|'.join([''.join(map(str, i)) for i in match_symbols])

        return generated_regex

