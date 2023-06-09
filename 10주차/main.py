score = '100,90,80,50'
scores = score.split(',')

total_scr = 0
avg_scr = 0.0


# for scr in scores:
#     total_scr += int(scr)



# total_scr = 0
# total_scr += int(scores[0])
# total_scr += int(scores[1])
# total_scr += int(scores[2])
# total_scr += int(scores[3])
# total_scr += int(scores[4])
# total_scr += int(scores[5])
# total_scr += int(scores[6])
# total_scr += int(scores[7])

# idx = 0
# total_scr += int(scores[idx])
# idx += 1
# total_scr += int(scores[idx])
# idx += 1
# total_scr += int(scores[idx])
# idx += 1
# total_scr += int(scores[idx])
# idx += 1
# total_scr += int(scores[idx])
# idx += 1
# total_scr += int(scores[idx])
# idx += 1
# total_scr += int(scores[idx])
# idx += 1
# total_scr += int(scores[idx])

idx = 0
total_scr = 0

if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1
if idx < len(scores):
    total_scr += int(scores[idx])
    idx += 1



avg_scr = total_scr / len(scores)

print("총합 점쉬 ", total_scr)
print("평균 점수: ", avg_scr)


# 평균보다 높은 과목의 수와 그 평균

cnt_above = 0
avg_above = 0.0
idx = 0

if avg_scr < int(scores[idx]):
    cnt_above += 1
    avg_above += int(scores[idx])

idx += 1
if avg_scr < int(scores[idx]):
    cnt_above += 1
    avg_above += int(scores[idx])

idx += 1
if avg_scr < int(scores[idx]):
    cnt_above += 1
    avg_above += int(scores[idx])

idx += 1
if avg_scr < int(scores[idx]):
    cnt_above += 1
    avg_above += int(scores[idx])



avg_above = avg_above / cnt_above

print("평균보다 높은 과목 수: ", cnt_above)
print("평균보다 높은 과목 평균: ", avg_above)









