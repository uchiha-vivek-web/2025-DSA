

def convert_string(name:str):
    cleaned = ''.join(char.lower() for char in name  if char.isalnum())
    return cleaned


def check_pallidrome(name:str):
    cleaned = ''.join(char.lower()  for char in name if char.isalnum())
    print(cleaned)
    return cleaned==cleaned[::-1]

# two pointer method
def check_pallindrome1(name:str):
    cleaned=''.join(char.lower()  for char in name if char.isalnum())
    n=len(cleaned)
    start,end=0,n-1
    while start<=end:
        if cleaned[start]!=cleaned[end]:
            return False
        start+=1
        end-=1
    return True

if __name__=="__main__":
    name:str ="Was it a car or a cat I saw?"
    ans=check_pallidrome(name)
    ans1=check_pallindrome1(name)
    print(ans1)