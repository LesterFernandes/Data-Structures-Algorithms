def word_break(s: str, word_dict: list[str]):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in word_dict:
            if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break

    return dp[0]


s = "leetcode"
wordDict = ["leet", "code"]
# print(word_break(s, wordDict))
