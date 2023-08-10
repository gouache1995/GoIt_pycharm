def game(terra, power):
    for i in range(len(terra)):
        for j in range(len(terra[i])):
            if power >= terra[i][j]:
                power += terra[i][j]
            else:
                break
    return power