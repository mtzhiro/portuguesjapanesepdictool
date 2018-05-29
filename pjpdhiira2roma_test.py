# coding: UTF-8
from __future__ import unicode_literals # <-文字列を全てunicodeとして扱う。3系では必要なし
import codecs
import re

f_in  = codecs.open('test.dic', 'r', 'utf-8')
f_out = codecs.open('test_out.dic', 'w', 'utf-8')

lines = f_in.readlines() #読み込み
lines2 = []
for line in lines:
    line = line.replace('て','TE') #テキスト置換
    line = line.replace('き','KI') #テキスト置換
    line = line.replace('す','SU') #テキスト置換
    line = line.replace('と','TO') #テキスト置換
    line = re.sub(r'(\d)(?=(\d{3})+(?!\d))', r'\1,', line) #正規表現置換
    lines2.append(line) #別リストにする
else:
    f_out.write(''.join(lines2)) #書き込み
    f_in.close()
