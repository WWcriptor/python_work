"""
    package : 관련있는 파이썬 파일(모듈)들을 ㄱ능별로 분류하여 모아놓은 디렉터리
            패키지 안에는 __init__.py라는 파일이 있음
    
    __init__.py
        파이썬 패키지(구조화된 모듈 모음)라고 파이썬 시스템에 알려주는 역할
            > 파이썬2에서는 이 파일이 없으면 패키지로 인식X
            > 파이썬3부터는 이 파일이 없어도 패키지로 인식 가능
            > 실무에서는 이 파일을 넣는 것을 권장
        기능
            1. 패키지를 불러올 때 가장 먼저 자동 실행(초기화) 딱 한 번 실행
                > 패키지를 쓰기 전에 미리 설정해야 되는 것들
                    ex) DB 연결, 로그 기록 설정, 환경 변수 로드 등의 초기화 작업시 작성
            2. 패키지 가져오기(import) 경로를 단축
            3. 패키지 내의 비밀파일 등의 목록을 지정해 둘 수 있다.
                > 호출시 from package import * 등으로 사용
                > __all__ 변수에 공개할 파일 목록만 지정 가능                
    
"""
# 1
import package01.image.io_file.imgRead
import package01.image.io_file.imgSave

package01.image.io_file.imgRead.jpgRead()
package01.image.io_file.imgRead.pngRead()

package01.image.io_file.imgSave.jpgSave()
package01.image.io_file.imgSave.pngSave()

print("-"*30)

# 2
import package01.image.io_file.imgRead as imgRead
import package01.image.io_file.imgSave as imgSave

imgRead.jpgRead()
imgRead.pngRead()

imgSave.jpgSave()
imgSave.pngSave()

print("-"*30)

#3
from package01.image.io_file import imgRead, imgSave

imgRead.jpgRead()
imgRead.pngRead()

print("-"*30)

#4
from package01.image.io_file import imgRead as iR
iR.jpgRead()
iR.pngRead()

print("-"*30)

#5
from package01.image.io_file.imgRead import pngRead, jpgRead
jpgRead()
pngRead()

print("-"*30)

#6
from package01.image.io_file.imgRead import pngRead as pR
from package01.image.io_file.imgRead import jpgRead as jR

pR()
jR()