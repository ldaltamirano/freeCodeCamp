function fiboEvenSum(n) {
    let suma = 2
    let previousTerm1 = 1
    let previousTerm2 = 2
    let value = 3
    while (value <= n) {
        previousTerm1 = previousTerm2
        previousTerm2 = value
        value = previousTerm1 + previousTerm2
        if (value % 2 == 0) {
            suma += value
        }
    }

    return suma;
}

console.log(fiboEvenSum(8));
