// El numero que tiene como divisores los que van de 1 a n
function smallestMult(n) {
    let divisores = [1, 2];
    for (let i = 3; i <= n; i++) {
        divisores.push(i);
    }
    let esDivisible = false;
    let number = n;
    while (!esDivisible) {
        esDivisible = true;
        number++;
        let div = divisores.find(x => number % x != 0);
        if (div > 1) {
            esDivisible = false;
        }
    }

    return number;
}