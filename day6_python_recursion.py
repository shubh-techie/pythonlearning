
def IsPalindrome(srt, start, end):
    if start >= end:
        return True
    if srt[start] != srt[end]:
        return False
    return IsPalindrome(srt, start + 1, end - 1)

def Pnindrome(srt):
    return IsPalindrome(srt, 0, len(srt) - 1)