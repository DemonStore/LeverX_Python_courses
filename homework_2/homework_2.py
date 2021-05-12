class Version:
    """При сравнении классов принято, что в названии версии
    "alpha" эквивалентно "a", "beta" эквивалентно "b"   """
    def __init__(self, version):
        self.version = version
        new_string = version[:]
        new_string = new_string.replace('-', '.')
        dict_for_change_one = {
            'alpha': '0',
            'beta': '1',
            'rc': '2'
        }
        dict_for_change_two = {
            'a': '.0',
            'b': '.1'
        }
        for key, value in dict_for_change_one.items():
            if key in new_string:
                new_string = new_string.replace(key, value)
        for key, value in dict_for_change_two.items():
            if key in new_string:
                new_string = new_string.replace(key, value)

        symbol_list = new_string.split('.')
        self.list_version = []
        for symbol in symbol_list:
            self.list_version.append(int(symbol))
        self.lenth = len(self.list_version)
    
    def __gt__(self, other_obj):
        if (self.list_version == other_obj.list_version[:3]) \
                and (other_obj.lenth > self.lenth):
            return True
        elif (self.list_version[:3] == other_obj.list_version) \
                and (other_obj.lenth < self.lenth):
            return False
        else:
            for my, foreign in zip(self.list_version, other_obj.list_version):
                if my > foreign:
                    return True
                elif my < foreign:
                    return False
    
    def __lt__(self, other_obj):
        result = self.__gt__(other_obj)
        return not result

    def __eq__(self, othet_obj):
        if (self.list_version == othet_obj.list_version):
            return True
        else:
            return False
    
    def __ne__(self, other_obj):
        result = self.__eq__(other_obj)
        return not result

def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()