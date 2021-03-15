import sys

for line in sys.stdin:
    sys.stdout.write("%s" % line)
    # 입력을 받고, Ctrl+D를 누른 뒤 enter키를 누르면 결과가 뜸
    # 입력을 받은 줄 수 만큼 반복하여 한 줄씩 출력
