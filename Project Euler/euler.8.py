data = "731671765313306249192251196744265747423553491949349698352031277450\
63262395783180169848018694788518438586156078911294949545950173795833195285\
32088055111254069874715852386305071569329096329522744304355766896648950445\
24452316173185640309871112172238311362229893423380308135336276614282806444\
48664523874930358907296290491560440772390713810515859307960866701724271218\
83998797908792274921901699720888093776657273330010533678812202354218097512\
54540594752243525849077116705560136048395864467063244157221553975369781797\
78461740649551492908625693219784686224828397224137565705605749026140797296\
86524145351004748216637048440319989000889524345065854122758866688116427171\
47992444292823086346567481391912316282458617866458359124566529476545682848\
91288314260769004224219022671055626321111109370544217506941658960408071984\
03850962455444362981230987879927244284909188845801561660979191338754992005\
24063689912560717606058861164671094050775410022569831552000559357297257163\
6269561882670428252483600823257530420752963450"

def largest_product(data, length):
    current = 0
    for i in xrange(0, len(data) - length):
        part= data[i:i+length]
        product = 1
        for char in part:
            product *= int(char)
        if product > current:
            current = product
    return current


if __name__ == "__main__":
    print str(largest_product(data, 13))
