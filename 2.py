filepath = 'C:/Users/peter/Curators/2.txt'
with open(filepath) as file:
    n, memory = [int(s) for s in file.readline().split(' ')]
    videos, memes = [], []
    for line in file:
        content, amount = line.split(' ')
        amount = int(amount)
        if content == 'video':
            videos.append(amount)
        else:
            memes.append(amount)
    videos.sort()
    memes.sort()
    curr_memory = int(memory)
    for video in videos:
        if (curr_memory - video) >= 0:
            curr_memory -= video
        else:
            break
    count = 0
    for meme in memes:
        if (curr_memory - meme) >= 0:
            curr_memory -= meme
            count += 1
        else:
            break
    print(curr_memory, count)
