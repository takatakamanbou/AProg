##### AProg2021 第7回課題A

# このプログラムを修正・変更してはいけません

import ex07score

name, scoreX, scoreY = ex07score.readData('ex07score.txt')

i, j = ex07score.argMinMax(scoreX)
print('1つめの試験の点数の最小:', name[i], scoreX[i])
print('1つめの試験の点数の最大:', name[j], scoreX[j])

i, j = ex07score.argMinMax(scoreY)
print('2つめの試験の点数の最小:', name[i], scoreY[i])
print('2つめの試験の点数の最大:', name[j], scoreY[j])