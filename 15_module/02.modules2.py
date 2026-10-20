# 1
# import 폴더명.모듈명

import modules.my_moduel2
modules.my_moduel2.my_func2()


# 2
# import 폴더명.모듈명 as 별칭
import modules.my_moduel2 as mo
mo.my_func2()

# 3
# from 폴더명.모듈명 import 함수명
from modules.my_moduel2 import my_func2
my_func2()

# 4
# from 폴더명.모듈명 import 함수명 as 별칭
from modules.my_moduel2 import my_func2 as mf2
mf2()