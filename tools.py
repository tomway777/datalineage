from re import sub

class spliters:
    def reformat(self, sql):
        uncomment = sub(r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/',"" ,sql)
        noline = sub(r'\n', '', uncomment)
        nodoublespace = noline.replace('    ','')

        return nodoublespace
    
    def split_sql(self, sql):
        nonwline = sub(r'\n', '', sql)
        nospace = nonwline.replace('   ','')
        nospace = nospace.replace('  ',' ')
        stripstr = nospace.rstrip('\n')
        splt = stripstr.split(' ')

        return splt


class parsers:

    def __init__(self, parameter_list):
        self.param_list = parameter_list
        super().__init__()

    def proc_parser(self, key_input):
        get_key = self.param_list.__contains__(key_input)
        if get_key == True:
            narray = []

            for item in self.param_list:
                get_tbl_name = item.__getitem__(get_key.__index__() + 1)
                if get_tbl_name != 'select' and get_tbl_name != 'set' and get_tbl_name != '(' and get_tbl_name != '@':
                    narray.append(get_tbl_name)

            return narray
################################################################################################################################
    # def get_from(self, parameter_list):
    #     get_key = parameter_list.__contains__('from')
    #     if get_key == True:
    #         narray = []

    #         for item in parameter_list:
    #             get_tbl_name = item.__getitem__(get_key.__index__() + 1)
    #             if get_tbl_name != 'select' and get_tbl_name != 'set' and get_tbl_name != '(' and get_tbl_name != '@':
    #                 narray.append(get_tbl_name)

    #         return narray