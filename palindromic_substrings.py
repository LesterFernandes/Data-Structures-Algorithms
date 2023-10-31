def countSubstrings(strr: str) -> int:
    count = 0
    for i in range(len(strr)):
        s, e = i, i
        while s in range(len(strr)) and e in range(len(strr)):
            if strr[s] != strr[e]:
                break
            count += 1
            s -= 1
            e += 1

        s, e = i, i + 1
        while s in range(len(strr)) and e in range(len(strr)):
            if strr[s] != strr[e]:
                break
            count += 1
            s -= 1
            e += 1

    return count
# print(countSubstrings("aaa")) --> 6
# print(countSubstrings("racecar")) --> 10
