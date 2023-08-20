function esPalindromo(str) {
    for (let index = 0; index < str.length; index++) {
        if (str[index] != str[str.length - index - 1]) {
            return false;
        }
    }

    return true;
}

function largestPalindromeProduct(n) {
    let semilla = Math.pow(10, n - 1);
    let limite = Math.pow(10, n);
    let maxValue = semilla;

    for (let i = semilla; i < limite; i++) {
        for (let j = semilla; j < limite; j++) {
            if (esPalindromo((i * j).toString()) && maxValue < (i * j)) {
                maxValue = (i * j);
            }
        }
    }

    return maxValue;
}

largestPalindromeProduct(2);