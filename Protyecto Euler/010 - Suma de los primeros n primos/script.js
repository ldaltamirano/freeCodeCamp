function esPrimo(n, i = 2) {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % i === 0) return false;
    if (i * i > n) return true;
    return esPrimo(n, i + 1);
}

function primeSummation(n) {
    let digitosPrimos = [];
    
    for (let index = 2; index < n; index++) {
        if (esPrimo(index)) {
            digitosPrimos.push(index);   
        }     
    }
    
    let total = digitosPrimos.reduce((a, b) => a + b, 0);

    return total;
}

primeSummation(2000000)

