with open("2022/data/8.txt") as f:
    content = [list(map(int, list(x))) for x in f.read().split("\n")[:~0]]
    flip_content = list(zip(*content))

total = 0
max_score = 0
for i in range(len(content)):
    for j in range(len(content[0])):
        col = [content[x][j] for x in range(len(content))]

        l, r, u, d = (
            list(reversed(content[i][:j])),
            content[i][j + 1 :],
            list(reversed(col[:i])),
            col[i + 1 :],
        )
        if i == 0 or j == 0 or i == len(content) - 1 or j == len(content[0]) - 1:
            total += 1
        else:
            left, right = max(l), max(r)
            up, down = max(u), max(d)
            if content[i][j] > min(up, down, left, right):
                total += 1

        cum_score = 1
        for path in (l, r, u, d):
            score = 1
            for t in range(len(path)):
                if path[t] < content[i][j]:
                    score += 1
                else:
                    break
                if t == len(path) - 1:
                    score -= 1
            cum_score *= score

        if cum_score > max_score:
            max_score = cum_score


answer_one = total
answer_two = max_score
print("p1:", answer_one)
print("p2:", answer_two)
