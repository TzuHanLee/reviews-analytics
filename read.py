data = []
count = 0
with open('review.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  #count = count + 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完畢,總共有', len(data), '筆資料')
print('......................................')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len / len(data))
print('......................................')


new = [ ]
for d in data:
        if len(d) < 100:
                new.append(d)
print('一共有', len(new), '比留言長度小於100')
print('......................................')


bad = [ 'bad' in d for d in data]
print(bad)


#文字計數
wc = {}  #wc=word_count
for d in data:
    words =	d.split()  #split會切片成一塊塊的清單 #split這個功能預設值就是空白鍵
    for word in words:
    	if word in wc:
    	    wc[word] += 1 
    	else:
    		wc[word] = 1  #新增新的key進入wc字典


for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word]) #word[word]為那個字出現次數

print(len(wc))
print(wc['Allen'])	

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q': #q=quit停止
	    break
    if word in wc:
    	print(word, '出現的次數為: ', wc[word])
    else:
    	print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')    	

