"""
4. 불러들인 datetime모듈을 활용하여 현재 시각을 출력하시오.
"""
import datetime

###정답란###
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
