function esPrimo(n) {
    let index = 2;
    while (index != n) {
        if (n % index == 0) {
            return false;
        }
        index++;
    }
    return true;
}

function largestPrimeFactor(number) {
    let n = 2
    let maxPrimo = 1
    do {
        if (number % n == 0 && esPrimo(n) && n > maxPrimo) {
            maxPrimo = n
        }
        n++;

    } while (n <= number);

    return maxPrimo;
}

largestPrimeFactor(13195);