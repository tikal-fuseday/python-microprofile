import re


# Name of the Tag. Must match the regex [a-zA-Z_][a-zA-Z0-9_]#
# A required field which holds the name of the tag.
class Tag:
    PATTERN = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]')

    def __init__(self, name, value):
        # Constructs the Tag object with the given tag name and tag value
        #
        # tagName The tag name, must match the regex [a-zA-Z_][a-zA-Z0-9_]#.
        # tagValue The tag value
        # raises IllegalArgumentException If the tagName does not match [a-zA-Z_][a-zA-Z0-9_]#
        if not name or not value:
            raise Exception('Invalid arguments. Tag name: [{}], Tag value: [{}]'.format(name, value))

        if not Tag.PATTERN.match(name):
            raise Exception('Invalid Tag name: [{}]'.format(name))

        self.tagName = name
        self.tagValue = value

    def get_tag_name(self):
        return self.tagName

    def get_tag_value(self):
        return self.tagValue
