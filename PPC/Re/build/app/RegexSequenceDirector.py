from RegexSequence import *
from RegexGenerators import *
from random import randint, sample, shuffle
from itertools import product


class RegexSequenceDirector:
    def __init__(self, deviations, available_symbols, regex_generator_factory):
        """
        :param deviations:
        :param available_symbols: string of the available symbols to use
        :param regex_generator_factory: object of type RegexGeneratorFactory
        """
        self.deviations = deviations
        self.available_symbols = available_symbols
        self.regex_generator_factory = regex_generator_factory
        self.string = ''
        self.input_noise = {}

    def generate_regex(self, string, input_noise):
        """
        :param string: string to generate regex for, ie abc
        :param input_noise: dict of dicts of 2 lists of elements which can be inserted as noise in the regex for each
         position, first list is the positive noise (chars which can be matched against), the second one if for characters
         which could be explicitly matched against,
          ie with abc => { 'a' => {'positive' => ['w','q','t'],  'negative' => ['z','x','c'] }
        :returns RegexSequence
        """
        self.string = string
        self.input_noise = input_noise

        generator = self.regex_generator_factory[randint(0, len(self.regex_generator_factory) - 1)]
        generated_regex = ''
        if isinstance(generator, NoopRegexGenerator):
            generated_regex = generator.get_regex(self.string, '')
        elif isinstance(generator, CharacterSetGenerator):
            generated_regex = self.handle_character_set_generator(generator)
        elif isinstance(generator, AlternationGenerator):
            generated_regex = self.handle_alternation_generator(generator)
        return RegexSequence(self.string, generated_regex)

    def handle_character_set_generator(self, generator):
        """
        :param generator with type of characted set class
        :return: string: Generated regex
        """
        if randint(0, 1) is 0:  # positive match
            match_symbols = []
            match_symbols.extend([x for x in self.string])
            avail_noise =[x for key in self.input_noise for x in self.input_noise[key]['positive']]
            if len(avail_noise) < self.deviations:
                raise Exception('Not enough negative noise in handle_character_set_generator')
            match_symbols.extend(sample(avail_noise, self.deviations))
            shuffle(match_symbols)
            generated_regex = generator.get_regex(match_symbols, [])
        else:  # negative match
            dont_match_symbols = []
            avail_noise =[x for key in self.input_noise for x in self.input_noise[key]['negative']
                          if x not in self.string]
            if len(avail_noise) < self.deviations + len(self.string):  # TODO: validate this beforehand
                raise Exception('Not enough negative noise in handle_character_set_generator')
            dont_match_symbols.extend(sample(avail_noise, self.deviations + len(self.string)))
            shuffle(dont_match_symbols)
            generated_regex = generator.get_regex([], dont_match_symbols, negate=True)

        return generated_regex

    def handle_alternation_generator(self, generator):
        """
        :param generator with type of alternation class
        :return: string: Generated regex
        """
        match_symbols = [(list(self.string),)]
        avail_noise = []
        for index in self.input_noise:
            avail_noise.append([x for x in self.input_noise[index]['positive']])

        matches = sample(list(product(avail_noise)), self.deviations)
        match_symbols.extend(matches)

        shuffle(match_symbols)
        generated_regex = generator.get_regex([items[0] for items in match_symbols])

        return generated_regex
