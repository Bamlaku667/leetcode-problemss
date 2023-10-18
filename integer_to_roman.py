def intToRoman( num: int) -> str:
    dict = [
        ["I",1],
        ["IV", 4],
        ["V",5],
        ["IX",9],
        ["X",10],
        ["XL", 40],
        ["L",50],
        ["XC", 90],
        ["C",100],
        ["CD", 400],
        ["D",500],
        ["CM", 900],
        ["M",1000]
    ]
    str = ""
    for key, value in reversed(dict):
        if num // value:
            count = num // value
            str += key * count
            num = num % value

    return str

            

            