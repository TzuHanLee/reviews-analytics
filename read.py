data = []
count = 0
with open('review.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  #count = count + 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完畢,總共有', len(data), '筆資料')

