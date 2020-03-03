import re

# number_mapping = {'1': 'one',
#                   '2': 'two',
#                   '3': 'three', 
#                   '4' : ['one', 'otw', 'itw'] }
# s = "1 testing 2 3"

# # print (re.sub(r'\d', s, lambda x: number_mapping[x.group()]))
# # print(number_mapping)

# for k,v in number_mapping.items():
#     if k == '1':
#         print(v)



# for k,v in number_mapping.items():
#     if type(v) != str:
#         nls = []
#         for i in v:            
#             nls.append(re.sub(r'o', 'L', i))
#         number_mapping[k] = nls
# print(number_mapping)


ss = """
BEGIN

        CASE WHEN EXISTS(SELECT id FROM `btn_bansos`.`bansos_produk` WHERE id = input_id_produk AND status = 1)  THEN

                UPDATE `btn_bansos`.`bansos_produk`
                SET
                        `status` = 0,
            `deleted_by` = IFNULL(input_deleted_by, deleted_by)
                WHERE `id` = input_id_produk;

                SELECT a.code, a.message, a.note FROM `btn_bansos`.`bansos_error_message` AS a WHERE `a`.`code` = '00';

        ELSE

                SELECT a.code, a.message, a.note FROM `btn_bansos`.`bansos_error_message` AS a WHERE `a`.`code` = 'DBE03';

        END CASE;

/*---------------------------Audit Trail------------------------------/
# Created By    : April
# Created At    : 2019-03-11
# Updated By    : -
# Updated At    : -
# Desc                  : delete data produk (change status to 0)
/-------------------------------------------------------------------*/

END"""



nn = re.sub(r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/',"" ,ss)
nw = re.sub(r'\n', '', nn)
pres = nw.replace('   ','')
m = pres.replace('  ',' ')
psw = m.rstrip('\n')
ps = psw.split(' ')
print(ps)
# pres = nw.replace('   ','')
# ps = pres.split(' ')
# print(ps)


